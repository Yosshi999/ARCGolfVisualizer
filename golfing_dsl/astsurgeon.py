import ast

class RemoveTypeAnnotations(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        node.returns = None
        for arg in node.args.args:
            arg.annotation = None
        return node

class RemoveDocstrings(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        if len(node.body) > 0 and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Constant):
            node.body = node.body[1:]
        return node

def collect_called_functions(node: ast.FunctionDef, visited_funcnames: set, function_defs: dict):
    """Recursively collects all function calls in the AST node."""
    visited_funcnames.add(node.name)
    for n in ast.walk(node):
        if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load) and n.id in function_defs:
            if n.id not in visited_funcnames:
                defnode = function_defs[n.id]
                collect_called_functions(defnode, visited_funcnames, function_defs)

def collect_used_globals(node: ast.FunctionDef, global_defs: dict):
    out = set()
    for n in ast.walk(node):
        if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load) and n.id in global_defs:
            out.add(n.id)
    return out

class FoldConstants(ast.NodeTransformer):
    def __init__(self, constants: dict):
        super().__init__()
        self.constants = constants
    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load) and node.id in self.constants:
            return self.constants[node.id]
        return node

def minify(source: str) -> str:
    """Minifies the given source code.
    Args:
        source (str): The source code to minify.
    Returns:
        str: The minified source code.
    """
    tree = ast.parse(source)
    # remove type annotations
    tree = RemoveTypeAnnotations().visit(tree)
    # remove docstrings
    tree = RemoveDocstrings().visit(tree)
    # collect all function definitions
    function_defs = {node.name: node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)}
    # find p(g)
    p_function = function_defs['p']
    visited_funcnames = set()
    collect_called_functions(p_function, visited_funcnames, function_defs)
    # remove all functions that are not called by p(g)
    tree.body = list(filter(lambda node: not isinstance(node, ast.FunctionDef) or node.name in visited_funcnames, tree.body))

    global_defs = {node.targets[0].id: node.value for node in tree.body if isinstance(node, ast.Assign)}
    constant_defs = {k: v for k, v in global_defs.items() if isinstance(v, ast.Constant)}
    import_defs = {}
    for node in tree.body:
        if isinstance(node, ast.ImportFrom):
            import_defs[node.module] = set()
            for alias in node.names:
                global_defs[alias.name] = alias
                import_defs[node.module].add(alias.name)

    # fold constants
    tree = FoldConstants(constant_defs).visit(tree)
    
    # remove all globals that are not used
    visited_globals = set()
    for func in visited_funcnames:
        visited_globals |= collect_used_globals(function_defs[func], global_defs)

    new_body = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if node.targets[0].id in visited_globals:
                new_body.append(node)
        elif isinstance(node, ast.ImportFrom):
            if import_defs[node.module] & visited_globals:
                new_body.append(node)
        else:
            new_body.append(node)
    tree.body = new_body

    return ast.unparse(tree)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python astsurgeon.py <source_file>")
        sys.exit(1)
    
    source_file = sys.argv[1]
    with open(source_file, 'r') as f:
        source_code = f.read()
    
    minified_code = minify(source_code)
    print(minified_code)