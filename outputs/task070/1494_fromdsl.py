def ofcolor(grid, value):
    return frozenset(((i, j) for (i, r) in enumerate(grid) for (j, v) in enumerate(r) if v == value))

def ulcorner(patch):
    return tuple(map(min, zip(*toindices(patch))))

def lrcorner(patch):
    return tuple(map(max, zip(*toindices(patch))))

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

def index(grid, loc):
    (i, j) = loc
    (h, w) = (len(grid), len(grid[0]))
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]]

def backdrop(patch):
    if len(patch) == 0:
        return frozenset({})
    indices = toindices(patch)
    (si, sj) = ulcorner(indices)
    (ei, ej) = lrcorner(patch)
    return frozenset(((i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1)))

def delta(patch):
    if len(patch) == 0:
        return frozenset({})
    return backdrop(patch) - toindices(patch)

def p(g):
    return [list(v) for v in solve_32597951(tuple((tuple(r) for r in g)))]

def solve_32597951(I):
    x1 = ofcolor(I, 8)
    x2 = delta(x1)
    O = fill(I, 3, x2)
    return O