def merge(containers):
    return type(containers)((e for c in containers for e in c))

def apply(function, container):
    return type(container)((function(e) for e in container))

def mapply(function, container):
    return merge(apply(function, container))

def ofcolor(grid, value):
    return frozenset(((i, j) for (i, r) in enumerate(grid) for (j, v) in enumerate(r) if v == value))

def toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((index for (value, index) in patch))
    return patch

def dneighbors(loc):
    return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})

def ineighbors(loc):
    return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})

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

def p(g):
    return [list(v) for v in solve_b60334d2(tuple((tuple(r) for r in g)))]

def solve_b60334d2(I):
    x1 = ofcolor(I, 5)
    x2 = replace(I, 5, 0)
    x3 = mapply(dneighbors, x1)
    x4 = mapply(ineighbors, x1)
    x5 = fill(x2, 1, x3)
    O = fill(x5, 5, x4)
    return O