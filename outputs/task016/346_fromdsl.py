def switch(grid, a, b):
    return tuple((tuple((v if v != a and v != b else {a: b, b: a}[v] for v in r)) for r in grid))

def p(g):
    return [list(v) for v in solve_0d3d703e(tuple((tuple(r) for r in g)))]

def solve_0d3d703e(I):
    x1 = switch(I, 3, 4)
    x2 = switch(x1, 8, 9)
    x3 = switch(x2, 2, 6)
    O = switch(x3, 1, 5)
    return O