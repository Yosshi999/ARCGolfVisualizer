def replace(grid, replacee, replacer):
    return tuple((tuple((replacer if v == replacee else v for v in r)) for r in grid))

def p(g):
    return [list(v) for v in solve_b1948b0a(tuple((tuple(r) for r in g)))]

def solve_b1948b0a(I):
    O = replace(I, 6, 2)
    return O