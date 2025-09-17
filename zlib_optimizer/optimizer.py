from ast_unparse import unparse
from var_conflict import construct_collision_graph
from zip_src import zip_src

import ast
from typing import List, Set, Dict
from collections import Counter
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
        

def optimize_code(src: str) -> str:
    """
    Optimize the given Python source code by renaming variables to minimize ZLIB-compressed size.

    Args:
        src (str): The input Python source code as a string.

    Returns:
        str: The optimized Python source code with renamed variables.
    """
    tree = ast.parse(src)
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

    new_tree = VariableRenamer(mapper).visit(tree)
    new_src = unparse(new_tree)
    return new_src, mapper


if __name__ == "__main__":
    src = """r=range
f=lambda g:[y for y,v in enumerate(g)if any(v)]
def p(g):
 h,w=f(g),f(zip(*g))
 for t in r(36):
  for k in r((h[1]-h[0])//2)[1::2]:g[h[a:=t//2%2]+(k+1)*(1-2*a)][w[b:=t%2]]=5
  for k in r((w[1]-w[0])//2)[1::2]:g[h[b]][w[a]+(k+1)*(1-2*a)]=5
  if(Y:=t//4%3-1)|(X:=t//12%3-1):g[h[b]+Y][w[a]+X]=g[h[~b]][w[a]]
 return g""".strip().replace("\r","")

    optimized_src, mapper = optimize_code(src)

    orig_zipped = zip_src(src.encode())
    optim_zipped = zip_src(optimized_src.encode())
    print("=== Mapper ===")
    print(mapper)
    print("=== Original ===")
    print(src)
    print("=== Optimized ===")
    print(optimized_src)
    print("=== Size Comparison ===")
    print(f"Original: {len(src)} bytes, ZLIB-compressed: {len(orig_zipped)} bytes")
    print(f"Optimized: {len(optimized_src)} bytes, ZLIB-compressed: {len(optim_zipped)} bytes")