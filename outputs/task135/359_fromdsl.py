THREE_BY_THREE = (3, 3)

def tojvec(j):
    return (0, j)

def crop(grid, start, dims):
    return tuple((r[start[1]:start[1] + dims[1]] for r in grid[start[0]:start[0] + dims[0]]))

def p(g):
    return [list(v) for v in solve_5bd6f4ac(tuple((tuple(r) for r in g)))]

def solve_5bd6f4ac(I):
    x1 = tojvec(6)
    O = crop(I, x1, THREE_BY_THREE)
    return O