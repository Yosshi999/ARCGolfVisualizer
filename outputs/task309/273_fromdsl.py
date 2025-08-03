def replace(grid, replacee, replacer):
    return tuple((tuple((replacer if v == replacee else v for v in r)) for r in grid))

def p(g):
    return [list(v) for v in solve_c8f0f002(tuple((tuple(r) for r in g)))]

def solve_c8f0f002(I):
    O = replace(I, 7, 5)
    return O