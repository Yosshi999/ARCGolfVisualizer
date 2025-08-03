def first(container):
    return next(iter(container))

def last(container):
    return max(enumerate(container))[1]

def remove(value, container):
    return type(container)((e for e in container if e != value))

def ofcolor(grid, value):
    return frozenset(((i, j) for (i, r) in enumerate(grid) for (j, v) in enumerate(r) if v == value))

def crop(grid, start, dims):
    return tuple((r[start[1]:start[1] + dims[1]] for r in grid[start[0]:start[0] + dims[0]]))

def toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((index for (value, index) in patch))
    return patch

def fill(grid, value, patch):
    (h, w) = (len(grid), len(grid[0]))
    grid_filled = list((list(row) for row in grid))
    for (i, j) in toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_filled[i][j] = value
    return tuple((tuple(row) for row in grid_filled))

def hsplit(grid, n):
    (h, w) = (len(grid), len(grid[0]) // n)
    offset = len(grid[0]) % n != 0
    return tuple((crop(grid, (0, w * i + i * offset), (h, w)) for i in range(n)))

def index(grid, loc):
    (i, j) = loc
    (h, w) = (len(grid), len(grid[0]))
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]]

def p(g):
    return [list(v) for v in solve_cf98881b(tuple((tuple(r) for r in g)))]

def solve_cf98881b(I):
    x1 = hsplit(I, 3)
    x2 = first(x1)
    x3 = remove(x2, x1)
    x4 = first(x3)
    x5 = last(x3)
    x6 = ofcolor(x4, 9)
    x7 = ofcolor(x2, 4)
    x8 = fill(x5, 9, x6)
    O = fill(x8, 4, x7)
    return O