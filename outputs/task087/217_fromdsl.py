def rot180(grid):
    return tuple((tuple(row[::-1]) for row in grid[::-1]))

def p(g):
    return [list(v) for v in solve_3c9b0459(tuple((tuple(r) for r in g)))]

def solve_3c9b0459(I):
    O = rot180(I)
    return O