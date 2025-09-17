import ast
from dataclasses import dataclass, field
import heapq
from typing import List, Optional, Tuple, Union, Set, Dict
from contextlib import contextmanager
import keyword
import builtins

from ast_unparse import unparse

@dataclass
class CFN:
    """Node in a control flow graph (CFG)."""
    parents: List["CFN"]
    children: List["CFN"]
    uevar: Set[str]  # Upward Exposure Variables
    varkill: Set[str]  # Variables killed (redefined) in this node
    liveout: Set[str]  # Variables live on exit
    minimum_env: Set[str] = field(default_factory=set)  # FOR DEBUG: minimum variables defined in the node

    def append_child(self, child: "CFN"):
        self.children.append(child)
        child.parents.append(self)


def collect_free_vars(root: CFN) -> Set[str]:
    # Resolve function call uevar
    minimum_vars: Dict[int, Set[str]] = {}  # minumum defined vairables at beginning in each node
    externals: Set[str] = set()  # variables used but not defined in this scope
    @dataclass(order=True)
    class Item:
        size: int
        node: CFN = field(compare=False)
        prev_vars: Set[str] = field(compare=False, default_factory=set)
    queue = [Item(0, root, set())]
    heapq.heapify(queue)
    while queue:
        item = heapq.heappop(queue)
        node = item.node
        if id(node) in minimum_vars and (minimum_vars[id(node)] & item.prev_vars) == minimum_vars[id(node)]:
            # no update
            continue
        if id(node) not in minimum_vars:
            minimum_vars[id(node)] = set(item.prev_vars)
        else:
            minimum_vars[id(node)] &= item.prev_vars
        # add newly defined variables
        current_vars = node.varkill | minimum_vars[id(node)]
        node.minimum_env = set(current_vars)
        # add used but not defined variables to externals
        externals |= node.uevar - current_vars

        for child in node.children:
            heapq.heappush(queue, Item(len(current_vars), child, current_vars))
    return externals


class CFGConstructor(ast.NodeVisitor):
    def __init__(self):
        self._graph = CFN(parents=[], children=[], uevar=set(), varkill=set(), liveout=set())
        self._subgraph: Dict[str, CFN] = {}
        self._scope_stack: List[CFN] = []
        self._function_callers: List[Tuple[str, CFN]] = []  # (function name, caller node) to resolve uevar later
        self._anon_counter = 0  # for anonymous scopes
        self._prev = self._graph
    
    def visit(self, node: ast.AST) -> CFN:
        self.traverse(node)
        return self._graph, self._subgraph
    
    def traverse(self, node: Union[ast.AST, List[ast.AST]]):
        if isinstance(node, list):
            for item in node:
                self.traverse(item)
        else:
            super().visit(node)
    
    @contextmanager
    def scope(self, name: Optional[str] = None):
        """Isolate a new scope for functions, classes, comprehensions, etc."""
        if name is None:
            name = f"anon-{self._anon_counter}"
            self._anon_counter += 1
        self._scope_stack.append(self._prev)
        subgraph = CFN(parents=[], children=[], uevar=set(), varkill=set(), liveout=set())
        self._prev = subgraph
        yield name
        self._subgraph[name] = subgraph

        externals = collect_free_vars(subgraph)
        subgraph.uevar |= externals

        # Update callers
        resolved = []
        for i, (func_name, caller) in enumerate(self._function_callers):
            if func_name == name:
                caller.uevar |= externals
                resolved.append(i)
        for i in reversed(resolved):
            self._function_callers.pop(i)

        self._prev = self._scope_stack.pop()
    
    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self._prev.append_child(
                CFN(parents=[], children=[], uevar={node.id}, varkill=set(), liveout=set())
            )
            self._prev = self._prev.children[-1]
        elif isinstance(node.ctx, (ast.Store, ast.Del)):
            self._prev.append_child(
                CFN(parents=[], children=[], uevar=set(), varkill={node.id}, liveout=set())
            )
            self._prev = self._prev.children[-1]
        else:
            raise NotImplementedError(f"Unknown context {node.ctx} for Name")
    
    def visit_Assign(self, node):
        if len(node.targets) == 1 and isinstance(node.targets[0], ast.Name) and isinstance(node.value, ast.Lambda):
            # Lambda assignment (e.g. f = lambda x: x+1)
            # Record it as a function f
            self._trackable_lambda(node.value, node.targets[0].id)
        else:
            self.traverse(node.value)
        for target in node.targets:
            self.traverse(target)
    
    def visit_AnnAssign(self, node):
        if node.value:
            self.traverse(node.value)
        self.traverse(node.target)
    
    def visit_NamedExpr(self, node):
        self.traverse(node.value)
        self.traverse(node.target)
    
    def visit_AugAssign(self, node):
        """x += v
        Load(x); Load(v); Store(x)
        """
        if isinstance(node.target, ast.Name):
            # target is single.
            self._prev.append_child(
                CFN(parents=[], children=[], uevar={node.target.id}, varkill=set(), liveout=set())
            )
            self._prev = self._prev.children[-1]
            self.traverse(node.value)
            self._prev.append_child(
                CFN(parents=[], children=[], uevar=set(), varkill={node.target.id}, liveout=set())
            )
            self._prev = self._prev.children[-1]
        elif isinstance(node.target, ast.Subscript):
            # only support subscript chain like a[i][j]...
            v = node.target.value
            stack = [node.target.slice]
            while True:
                if isinstance(v, ast.Subscript):
                    stack.append(v.slice)
                    v = v.value
                elif isinstance(v, ast.Name):
                    break
                else:
                    raise NotImplementedError(f"Unsupported AugAssign target {unparse(node)} at L{node.lineno}")
            assert isinstance(v, ast.Name)
            self._prev.append_child(
                CFN(parents=[], children=[], uevar={v.id}, varkill=set(), liveout=set())
            )
            self._prev = self._prev.children[-1]
            for s in reversed(stack):
                self.traverse(s)
            self._prev.append_child(
                CFN(parents=[], children=[], uevar=set(), varkill={v.id}, liveout=set())
            )
            self._prev = self._prev.children[-1]
        else:
            raise NotImplementedError(f"Unsupported AugAssign {unparse(node)} at L{node.lineno}")
        
    def visit_Try(self, node):
        raise NotImplementedError()
    
    def visit_TryStar(self, node):
        raise NotImplementedError()
    
    def visit_ClassDef(self, node):
        raise NotImplementedError()

    def visit_FunctionDef(self, node):
        self._function_helper(node)
    
    def visit_AsyncFunctionDef(self, node):
        self._function_helper(node)
    
    def _function_helper(self, node):
        self._prev.append_child(
            CFN(parents=[], children=[], uevar=set(), varkill={node.name}, liveout=set())
        )
        self._prev = self._prev.children[-1]
        with self.scope(node.name):
            for arg in node.args.args:
                self._prev.varkill.add(arg.arg)
            if node.args.vararg:
                self._prev.varkill.add(node.args.vararg.arg)
            if node.args.kwarg:
                self._prev.varkill.add(node.args.kwarg.arg)
            self.traverse(node.body)
    
    def visit_Lambda(self, node):
        raise NotImplementedError(f"Untrackable lambda function at L{node.lineno}")
    
    def _trackable_lambda(self, node, assigned_name: str):
        with self.scope(assigned_name):
            for arg in node.args.args:
                self._prev.varkill.add(arg.arg)
            if node.args.vararg:
                self._prev.varkill.add(node.args.vararg.arg)
            if node.args.kwarg:
                self._prev.varkill.add(node.args.kwarg.arg)
            self.traverse(node.body)
    
    def visit_alias(self, node):
        if node.asname:
            self._prev.varkill.add(node.asname)
        else:
            self._prev.varkill.add(node.name)
    
    def visit_For(self, node):
        self._for_helper(node)
    def visit_AsyncFor(self, node):
        self._for_helper(node)
    
    def _for_helper(self, node):
        self._prev.append_child(
            CFN(parents=[], children=[], uevar=set(), varkill=set(), liveout=set())
        )
        cond_head = self._prev.children[-1]
        self._prev = cond_head
        self.traverse(node.iter)
        self.traverse(node.target)
        cond_tail = self._prev
        self.traverse(node.body)
        self._prev.append_child(cond_head)  # loop back
        self._prev = cond_tail
        if node.orelse:
            self.traverse(node.orelse)
    
    def visit_If(self, node):
        self.traverse(node.test)
        branch_head = self._prev
        self.traverse(node.body)
        branch_ends = [self._prev]
        # collapse nested ifs into equivalent elifs
        while node.orelse and len(node.orelse) == 1 and isinstance(node.orelse[0], ast.If):
            node = node.orelse[0]
            self._prev = branch_head
            self.traverse(node.test)
            branch_head = self._prev
            self.traverse(node.body)
            branch_ends.append(self._prev)
        # final else
        if node.orelse:
            self._prev = branch_head
            self.traverse(node.orelse)
            branch_ends.append(self._prev)
        # merge branches
        if len(branch_ends) > 1:
            merge_node = CFN(parents=[], children=[], uevar=set(), varkill=set(), liveout=set())
            for end in branch_ends:
                end.append_child(merge_node)
            self._prev = merge_node
        else:
            self._prev = branch_ends[0]

    def visit_While(self, node):
        self._prev.append_child(
            CFN(parents=[], children=[], uevar=set(), varkill=set(), liveout=set())
        )
        cond_head = self._prev.children[-1]
        self._prev = cond_head
        self.traverse(node.test)
        cond_tail = self._prev
        self.traverse(node.body)
        self._prev.append_child(cond_head)  # loop back
        self._prev = cond_tail
        if node.orelse:
            self.traverse(node.orelse)
    
    def visit_With(self, node):
        self.traverse(node.items)
        self.traverse(node.body)
    def visit_AsyncWith(self, node):
        self.traverse(node.items)
        self.traverse(node.body)

    def visit_IfExp(self, node):
        self.traverse(node.test)
        branch_head = self._prev
        self.traverse(node.body)
        if node.orelse:
            branch_ends = [self._prev]
            self._prev = branch_head
            self.traverse(node.orelse)
            branch_ends.append(self._prev)
            merge_node = CFN(parents=[], children=[], uevar=set(), varkill=set(), liveout=set())
            for end in branch_ends:
                end.append_child(merge_node)
            self._prev = merge_node
    
    def visit_ListComp(self, node):
        with self.scope() as funcname:
            self._generator_helper(node.generators)
            self.traverse(node.elt)
        self._prev.append_child(
            CFN(parents=[], children=[], uevar=set(self._subgraph[funcname].uevar), varkill=set(), liveout=set())
        )
        self._prev = self._prev.children[-1]
    def visit_SetComp(self, node):
        with self.scope() as funcname:
            self._generator_helper(node.generators)
            self.traverse(node.elt)
        self._prev.append_child(
            CFN(parents=[], children=[], uevar=set(self._subgraph[funcname].uevar), varkill=set(), liveout=set())
        )
        self._prev = self._prev.children[-1]
    def visit_GeneratorExp(self, node):
        # Not supported due to complexity of tracking evaluation
        raise NotImplementedError("Generator expressions are not supported")
    def visit_DictComp(self, node):
        with self.scope() as funcname:
            self._generator_helper(node.generators)
            self.traverse(node.key)
            self.traverse(node.value)
        self._prev.append_child(
            CFN(parents=[], children=[], uevar=set(self._subgraph[funcname].uevar), varkill=set(), liveout=set())
        )
        self._prev = self._prev.children[-1]
    
    def _generator_helper(self, generators: List[ast.comprehension]):
        for gen in generators:
            self.traverse(gen.iter)
            self.traverse(gen.target)
            for if_clause in gen.ifs:
                self.traverse(if_clause)
    
    def visit_Call(self, node):
        for arg in node.args:
            self.traverse(arg)
        for kw in node.keywords:
            self.traverse(kw)
        self.traverse(node.func)
        if isinstance(node.func, ast.Name):
            if node.func.id in self._subgraph:
                self._prev.append_child(
                    CFN(parents=[], children=[], uevar=set(self._subgraph[node.func.id].uevar), varkill=set(), liveout=set())
                )
                self._prev = self._prev.children[-1]
            else:
                # resolve later
                self._function_callers.append((node.func.id, self._prev))
        else:
            print("Warning: Unresolvable function call", unparse(node), "at Line", node.lineno)
    
    def visit_TypeVar(self, node):
        raise NotImplementedError()
    def visit_TypeVarTuple(self, node):
        raise NotImplementedError()
    def visit_ParamSpec(self, node):
        raise NotImplementedError()
    def visit_TypeAlias(self, node):
        raise NotImplementedError()

def calculate_liveout(root: CFN):
    """Calculate liveout sets for each node in the CFG."""
    changed = True
    while changed:
        changed = False
        stack = [root]
        visited = set()
        while stack:
            node = stack.pop()
            if id(node) in visited:
                continue
            visited.add(id(node))
            old_liveout = set(node.liveout)
            # liveout = union of uevar and (liveout - varkill) of children
            new_liveout = set()
            for child in node.children:
                new_liveout |= child.uevar | (child.liveout - child.varkill)
                stack.append(child)
            node.liveout = new_liveout
            if old_liveout != node.liveout:
                changed = True

def collect_dependents(cfg: Dict[str, CFN]) -> Dict[str, Set[str]]:
    """Names of LiveOut and VarKill variables cannot be the same."""
    ret: Dict[str, Set[str]] = {}
    for g in cfg.values():
        stack = [g]
        visited = set()
        while stack:
            node = stack.pop()
            if id(node) in visited:
                continue
            visited.add(id(node))
            cluster = node.liveout | node.varkill
            for name in cluster:
                if name not in ret:
                    ret[name] = set()
                ret[name].update(cluster - {name})
            for child in node.children:
                stack.append(child)
    return ret

def construct_collision_graph(tree: ast.AST) -> Tuple[Dict[str, CFN], Dict[str, Set[str]]]:
    """Construct a control flow graph (CFG) and variable collision graph from an AST node."""
    constructor = CFGConstructor()
    graph, subgraphs = constructor.visit(tree)
    cfg = {
        "__main__": graph,
        **subgraphs
    }
    for g in cfg.values():
        calculate_liveout(g)

    collision = collect_dependents(cfg)
    if set(collision.keys()) & {"eval", "exec"}:
        raise NotImplementedError("The code uses eval/exec, which may introduce dynamic variable usage. Optimization aborted.")

    # remove reserved names and the entry point `p`
    reserved_names = set(keyword.kwlist) | set(dir(builtins)) | {"p"}
    collision = {
        key: value - reserved_names
        for key, value in collision.items()
        if key not in reserved_names
    }

    return cfg, collision

def visualize_cfg(cfg: Dict[str, CFN]) -> str:
    """Construct a control flow graph (CFG) from an AST node. Returns the root CFN."""
    visualized = ""
    visualized += f"```python\n{src}\n```\n"
    for name, g in cfg.items():
        visualized += name + "\n"
        visualized += "```mermaid\n"
        visualized += "graph TB\n"
        checked = set()
        def dfs(node: CFN):
            nonlocal visualized
            if id(node) in checked:
                return
            checked.add(id(node))
            label = f"\"ld({','.join(sorted(node.uevar))}) st({','.join(sorted(node.varkill))}) LO({','.join(sorted(node.liveout))}) ENV({','.join(sorted(node.minimum_env))})\""
            visualized += f'  N{id(node)}[{label}]\n'
            for child in node.children:
                visualized += f'  N{id(node)} --> N{id(child)}\n'
                dfs(child)
        dfs(g)
        visualized += "```\n"
    return visualized

if __name__ == "__main__":
    src = """
def p(g):
 i=0
 h=[v==i for u in g for v in u]
 c=sum(h)
 g=[[v * c + i for v in u] for u in g]
 return g
"""
    tree = ast.parse(src)
    cfg, collision = construct_collision_graph(tree)
    visualized = visualize_cfg(cfg)

    visualized += "## Variable Collision Graph\n"
    visualized += "```mermaid\ngraph TB\n"
    for var, conflicts in collision.items():
        for c in conflicts:
            if var < c:  # avoid duplicate edges
                visualized += f'  {var} --- {c}\n'
    visualized += "```\n"
    with open("graph.md", "w") as f:
        f.write(visualized)