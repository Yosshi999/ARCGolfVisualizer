def hconcat(a, b):
    return tuple((i + j for (i, j) in zip(a, b)))

def p(g):
    return [list(v) for v in solve_a416b8f3(tuple((tuple(r) for r in g)))]

def solve_a416b8f3(I):
    O = hconcat(I, I)
    return O