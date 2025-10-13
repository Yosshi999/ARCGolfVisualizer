from .ast_unparse import unparse
from .var_conflict import construct_collision_graph
from .zip_src import zip_src

import ast
from typing import List, Set, Dict
from collections import Counter, namedtuple
import string
import math
import copy

import numpy as np
import optuna
optuna.logging.set_verbosity(optuna.logging.WARNING)


class VariableRenamer(ast.NodeTransformer):
    def __init__(self, mapper: Dict[str, str]):
        self.mapper = mapper

    def visit_Name(self, node: ast.Name) -> ast.AST:
        if node.id in self.mapper:
            node.id = self.mapper[node.id]
            # return ast.copy_location(ast.Name(id=self.mapper[node.id], ctx=node.ctx), node)
        return node
    
    def visit_arg(self, node):
        if node.arg in self.mapper:
            node.arg = self.mapper[node.arg]
        return node

    def visit_FunctionDef(self, node):
        node = self.generic_visit(node)
        if node.name in self.mapper:
            node.name = self.mapper[node.name]
        return node

class RenameUnfolder(ast.NodeTransformer):
    """Unfold renaming such as r = range, where range is not assigned elsewhere (i.e., builtins)."""

    def __init__(self):
        self.candidates = {}  # dict name => (old node, dependents)
        self.reassigned_candidates = set()
        self.stored = set()
        self.mode = "collect"  # or "modify"
    def collect(self, node: ast.AST):
        self.mode = "collect"
        self.visit(node)
    def modify(self, node: ast.AST):
        self.mode = "modify"
        self.candidates = {
            k: v
            for k, v in self.candidates.items()
            if k not in self.reassigned_candidates and v[1].isdisjoint(self.stored)
        }
        return self.visit(node)
    def _unfold_attempt(self, node: ast.AST) -> bool:
        return len(node.targets) == 1 and isinstance(node.targets[0], ast.Name) and isinstance(node.value, (ast.Name, ast.Constant))
    def visit_Assign(self, node: ast.Assign) -> ast.AST:
        if self.mode == "collect":
            if self._unfold_attempt(node):
                target = node.targets[0].id
                value = node.value
                if target not in self.candidates:
                    if isinstance(value, ast.Name):
                        self.candidates[target] = (value, {value.id})
                    else:
                        self.candidates[target] = (value, set())
                    self.stored.add(target)
                else:
                    self.reassigned_candidates.add(target)  # multiple assignments
            else:
                self.generic_visit(node)
        elif self.mode == "modify":
            if self._unfold_attempt(node):
                target = node.targets[0].id
                if target in self.candidates:
                    return None  # remove this assignment
        return self.generic_visit(node)
    def visit_Name(self, node: ast.Name) -> ast.AST:
        if self.mode == "collect":
            if isinstance(node.ctx, ast.Store):
                self.stored.add(node.id)
        if self.mode == "modify":
            if isinstance(node.ctx, ast.Load) and node.id in self.candidates:
                # unfold
                value = self.candidates[node.id][0]
                return ast.copy_location(value, node)
        return node


def optimize_code(src: str, unfold_renaming = True, variable_renaming = True) -> str:
    """
    Optimize the given Python source code by renaming variables to minimize ZLIB-compressed size.

    Args:
        src (str): The input Python source code as a string.

    Returns:
        str: The optimized Python source code with renamed variables.
    """
    tree = ast.parse(src)

    if unfold_renaming:
        unfolder = RenameUnfolder()
        unfolder.collect(tree)
        tree = unfolder.modify(tree)
    
    if variable_renaming:
        _, collision, reserved_names = construct_collision_graph(tree)

        code_alphabets = Counter(src)
        name_alphabets = Counter()
        for node in ast.walk(tree):
            if isinstance(node, ast.Name) and node.id in collision:
                name_alphabets.update(node.id)

        possible_names = sorted(set(string.ascii_letters + "_") & set(code_alphabets) - reserved_names)
        variables = list(collision.keys())

        study = optuna.create_study(direction="minimize")
        def objective(trial: optuna.Trial) -> float:
            trial_tree = copy.deepcopy(tree)
            mapper = {}
            for v in variables:
                n = trial.suggest_categorical(v, list(possible_names))
                mapper[v] = n

            new_tree = VariableRenamer(mapper).visit(trial_tree)
            new_src = unparse(new_tree)
            zipped = zip_src(new_src.encode())
            cost = len(zipped)
            for u in collision.keys():
                for v in collision[u]:
                    if mapper[u] == mapper[v]:
                        cost += 10000  # penalty for conflict
            return cost
        study.optimize(objective, n_trials=100)
        print(f"Best zlib size: {study.best_trial.value}", study.best_trial.params)
        assert study.best_trial.value < 1000, "No feasible solution found"

        mapper = {}
        for v, n in study.best_trial.params.items():
            mapper[v] = n

        tree = VariableRenamer(mapper).visit(tree)

    new_src = unparse(tree)
    return new_src


if __name__ == "__main__":
    src = """
r=range
m=[-4,0,4]
def p(g):
 _,i,j=max((sum(v>0for u in g[i:i+3]for v in u[j:j+3]),i,j)for i in r(19)for j in r(19))
 for x in m:
  for y in m:
   I=i;J=j;c=max(g[i+x+q//3][j+y+q%3]for q in r(9))
   for k in r(27):
    if(q:=k%9)<1:I+=x;J+=y
    if 21>I+q//3>-1<J+q%3<21:g[I+q//3][J+q%3]=c*(g[i+q//3][j+q%3]>0)
 return g
""".strip().replace("\r","")

    sources = {
        "Original": src,
        "Variable Renaming": optimize_code(src, unfold_renaming=False),
        "Unfolding": optimize_code(src, variable_renaming=False),
        "Variable Renaming + Unfolding": optimize_code(src),
    }
    title_len = max(len(t) for t in sources)

    for title, s in sources.items():
        print(f"=== {title} ===")
        print(s)
    print("=== Size Comparison ===")
    for title, s in sources.items():
        zipped = zip_src(s.encode())
        print(f"{title + ' ' * (title_len - len(title))}: {len(s)} -> {len(zipped)} ({len(zipped)/len(s):.3%})")