def switch(grid, a, b):
    return tuple((tuple((v if v != a and v != b else {a: b, b: a}[v] for v in r)) for r in grid))

def p(g):
    return [list(v) for v in solve_d511f180(tuple((tuple(r) for r in g)))]

def solve_d511f180(I):
    O = switch(I, 5, 8)
    return O