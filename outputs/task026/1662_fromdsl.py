def intersection(a, b):
    return a & b

def ofcolor(grid, value):
    return frozenset(((i, j) for (i, r) in enumerate(grid) for (j, v) in enumerate(r) if v == value))

def toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((index for (value, index) in patch))
    return patch

def rot90(grid):
    return tuple((row for row in zip(*grid[::-1])))

def rot270(grid):
    return tuple((tuple(row[::-1]) for row in zip(*grid[::-1])))[::-1]

def fill(grid, value, patch):
    (h, w) = (len(grid), len(grid[0]))
    grid_filled = list((list(row) for row in grid))
    for (i, j) in toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_filled[i][j] = value
    return tuple((tuple(row) for row in grid_filled))

def replace(grid, replacee, replacer):
    return tuple((tuple((replacer if v == replacee else v for v in r)) for r in grid))

def index(grid, loc):
    (i, j) = loc
    (h, w) = (len(grid), len(grid[0]))
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]]

def tophalf(grid):
    return grid[:len(grid) // 2]

def bottomhalf(grid):
    return grid[len(grid) // 2 + len(grid) % 2:]

def lefthalf(grid):
    return rot270(tophalf(rot90(grid)))

def righthalf(grid):
    return rot270(bottomhalf(rot90(grid)))

def p(g):
    return [list(v) for v in solve_1b2d62fb(tuple((tuple(r) for r in g)))]

def solve_1b2d62fb(I):
    x1 = lefthalf(I)
    x2 = righthalf(I)
    x3 = ofcolor(x1, 0)
    x4 = ofcolor(x2, 0)
    x5 = intersection(x3, x4)
    x6 = replace(x1, 9, 0)
    O = fill(x6, 8, x5)
    return O