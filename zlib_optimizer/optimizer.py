from .ast_unparse import unparse
from .var_conflict import construct_collision_graph
from .zip_src import zip_src

import ast
from typing import List, Set, Dict
from collections import Counter, namedtuple
import string
import math

import openjij as oj
import jijmodeling as jm
import ommx_openjij_adapter as oj_ad
import numpy as np


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
        count_mult = {v: 0 for v in collision}
        for node in ast.walk(tree):
            if isinstance(node, ast.Name) and node.id in collision:
                name_alphabets.update(node.id)
                count_mult[node.id] += 1

        template_alphabets = code_alphabets - name_alphabets
        possible_names = sorted(set(string.ascii_letters + "_") & set(code_alphabets) - reserved_names)
        name_freq = {
            c: (template_alphabets[c] + 0.1) / len(src)
            for c in possible_names
        }
        name_cost = {
            c: -math.log2(freq)
            for c, freq in name_freq.items()
        }

        # Prepare QUBO
        V = jm.Placeholder("V")  # the number of nodes (variables)
        E = jm.Placeholder("E", ndim=2)  # the number of edges (collisions)
        N = jm.Placeholder("N")  # the number of colors (new variable names)
        C = jm.Placeholder("C", ndim=2)  # cost matrix (V x N)

        x = jm.BinaryVar("x", shape=(V, N))  # assignment
        v = jm.Element("v", (0, V))
        n = jm.Element("n", (0, N))
        e = jm.Element("e", E)
        problem = jm.Problem("Variable Renaming")
        problem += jm.Constraint("OneColorPerNode", x[v, :].sum() == 1, forall=v)
        problem += jm.Constraint("EdgeCollision", x[e[0], n] * x[e[1], n] == 0, forall=[e, n])
        problem += jm.sum([v, n], C[v, n] * x[v, n])

        variables = list(collision.keys())
        names = list(name_cost.keys())
        cost_matrix = np.array([*count_mult.values()])[:, None] * np.array([*name_cost.values()])[None, :]
        edge_matrix = np.array([[variables.index(u), variables.index(v)] for u in collision for v in collision[u]])

        instance_data = {
            "V": len(variables),
            "E": edge_matrix,
            "N": len(names),
            "C": cost_matrix / cost_matrix.max()
        }
        # compile
        instance = jm.Interpreter(instance_data).eval_problem(problem)
        # get qubo model
        qubo, const = instance.to_qubo()
        # set sampler
        sampler = oj.SASampler()
        # solve problem
        result = sampler.sample_qubo(qubo, num_reads=100)
        # decode result
        adapter = oj_ad.OMMXOpenJijSAAdapter(instance)
        sampleset = adapter.decode_to_sampleset(result)
        feasible_sample = sampleset.best_feasible_unrelaxed
        decision = feasible_sample.extract_decision_variables("x")
        mapper = {}
        for (v, n), val in decision.items():
            if val == 1:
                mapper[variables[v]] = names[n]

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