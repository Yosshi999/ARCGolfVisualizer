def first(container):
    return next(iter(container))

def crop(grid, start, dims):
    return tuple((r[start[1]:start[1] + dims[1]] for r in grid[start[0]:start[0] + dims[0]]))

def hsplit(grid, n):
    (h, w) = (len(grid), len(grid[0]) // n)
    offset = len(grid[0]) % n != 0
    return tuple((crop(grid, (0, w * i + i * offset), (h, w)) for i in range(n)))

def p(g):
    return [list(v) for v in solve_2dee498d(tuple((tuple(r) for r in g)))]

def solve_2dee498d(I):
    x1 = hsplit(I, 3)
    O = first(x1)
    return O