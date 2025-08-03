def rot180(grid):
    return tuple((tuple(row[::-1]) for row in grid[::-1]))

def p(g):
    return [list(v) for v in solve_6150a2bd(tuple((tuple(r) for r in g)))]

def solve_6150a2bd(I):
    O = rot180(I)
    return O