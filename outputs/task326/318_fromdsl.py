ORIGIN = (0, 0)
TWO_BY_TWO = (2, 2)

def crop(grid, start, dims):
    return tuple((r[start[1]:start[1] + dims[1]] for r in grid[start[0]:start[0] + dims[0]]))

def p(g):
    return [list(v) for v in solve_d10ecb37(tuple((tuple(r) for r in g)))]

def solve_d10ecb37(I):
    O = crop(I, ORIGIN, TWO_BY_TWO)
    return O