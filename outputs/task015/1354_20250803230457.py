def dneighbors(loc):
    return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})
def ineighbors(loc):
    return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})
def ofcolor(grid,value):
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)
def fill(grid,value,patch):
    h, w = len(grid), len(grid[0])
    grid_filled = list(list(row) for row in grid)
    for i, j in toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_filled[i][j] = value
    return tuple(tuple(row) for row in grid_filled)
def apply(function,container):
    return type(container)(function(e) for e in container)
def merge(containers):
    return type(containers)(e for c in containers for e in c)
def mapply(function,container):
    return merge(apply(function, container))
def toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset(index for value, index in patch)
    return patch
def p(g):
    I=tuple(tuple(r)for r in g)
    x1 = ofcolor(I, 1)
    x2 = ofcolor(I, 2)
    x3 = mapply(dneighbors, x1)
    x4 = mapply(ineighbors, x2)
    x5 = fill(I, 7, x3)
    O = fill(x5, 4, x4)
    return [list(r)for r in O]