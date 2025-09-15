import ast
from dataclasses import dataclass
from typing import List, Optional, Tuple, Union, Set, Dict
from contextlib import contextmanager

from ast_unparse import unparse

@dataclass
class CFN:
    """Node in a control flow graph (CFG)."""
    parents: List["CFN"]
    children: List["CFN"]
    uevar: Set[str]  # Upward Exposure Variables
    varkill: Set[str]  # Variables killed (redefined) in this node
    liveout: Set[str]  # Variables live on exit

    def append_child(self, child: "CFN"):
        self.children.append(child)
        child.parents.append(self)

class CFGConstructor(ast.NodeVisitor):
    def __init__(self):
        self._graph = CFN(parents=[], children=[], uevar=set(), varkill=set(), liveout=set())
        self._subgraph: Dict[str, CFN] = {}
        self._scope_stack: List[CFN] = []
        self.anon_counter = 0
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
        if name is None:
            name = f"anon-{self.anon_counter}"
            self.anon_counter += 1
        self._scope_stack.append(self._prev)
        subgraph = CFN(parents=[], children=[], uevar=set(), varkill=set(), liveout=set())
        self._prev = subgraph
        yield
        self._subgraph[name] = subgraph
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
        # target is always single.
        self._prev.append_child(
            CFN(parents=[], children=[], uevar={node.target.id}, varkill=set(), liveout=set())
        )
        self._prev = self._prev.children[-1]
        self.traverse(node.value)
        self._prev.append_child(
            CFN(parents=[], children=[], uevar=set(), varkill={node.target.id}, liveout=set())
        )
        self._prev = self._prev.children[-1]
        
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
        with self.scope():
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
        with self.scope():
            self._generator_helper(node.generators)
            self.traverse(node.elt)
    def visit_SetComp(self, node):
        with self.scope():
            self._generator_helper(node.generators)
            self.traverse(node.elt)
    def visit_GeneratorExp(self, node):
        with self.scope():
            self._generator_helper(node.generators)
            self.traverse(node.elt)
    def visit_DictComp(self, node):
        with self.scope():
            self._generator_helper(node.generators)
            self.traverse(node.key)
            self.traverse(node.value)
    
    def _generator_helper(self, generators: List[ast.comprehension]):
        for gen in generators:
            self.traverse(gen.iter)
            self.traverse(gen.target)
            for if_clause in gen.ifs:
                self.traverse(if_clause)
    
    def visit_TypeVar(self, node):
        raise NotImplementedError()
    def visit_TypeVarTuple(self, node):
        raise NotImplementedError()
    def visit_ParamSpec(self, node):
        raise NotImplementedError()
    def visit_TypeAlias(self, node):
        raise NotImplementedError()

def visualize_cfg(node: ast.AST) -> CFN:
    """Construct a control flow graph (CFG) from an AST node. Returns the root CFN."""
    constructor = CFGConstructor()
    graph, _ = constructor.visit(node)
    return graph, _

if __name__ == "__main__":
    src = """
R=range
def p(g):
 h=[v==0 for u in g for v in u]
 c=sum(h)
 g=[[v * c for v in u] for u in g]
 return g
"""
    tree = ast.parse(src)
    cfg, sub_cfgs = visualize_cfg(tree)
    cfg = {
        "__main__": cfg,
        **sub_cfgs
    }
    visualized = ""
    visualized += f"```python\n{src}\n```\n"
    for name, g in cfg.items():
        visualized += name + "\n"
        visualized += "```mermaid\n"
        visualized += "graph TB\n"
        checked = set()
        def dfs(node: CFN):
            global visualized
            if id(node) in checked:
                return
            checked.add(id(node))
            label = f"\"ld({','.join(sorted(node.uevar))}) st({','.join(sorted(node.varkill))}) LO({','.join(sorted(node.liveout))})\""
            visualized += f'  N{id(node)}[{label}]\n'
            for child in node.children:
                visualized += f'  N{id(node)} --> N{id(child)}\n'
                dfs(child)
        dfs(g)
        visualized += "```\n"
    
    with open("graph.md", "w") as f:
        f.write(visualized)