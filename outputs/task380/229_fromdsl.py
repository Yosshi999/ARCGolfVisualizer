def rot270(grid):
    return tuple((tuple(row[::-1]) for row in zip(*grid[::-1])))[::-1]

def p(g):
    return [list(v) for v in solve_ed36ccf7(tuple((tuple(r) for r in g)))]

def solve_ed36ccf7(I):
    O = rot270(I)
    return O