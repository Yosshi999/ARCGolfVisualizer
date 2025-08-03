def merge(containers):
    return type(containers)((e for c in containers for e in c))

def apply(function, container):
    return type(container)((function(e) for e in container))

def mapply(function, container):
    return merge(apply(function, container))

def mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for (v, _) in element]
    return max(set(values), key=values.count)

def leastcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for (v, _) in element]
    return min(set(values), key=values.count)

def ofcolor(grid, value):
    return frozenset(((i, j) for (i, r) in enumerate(grid) for (j, v) in enumerate(r) if v == value))

def toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((index for (value, index) in patch))
    return patch

def ineighbors(loc):
    return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})

def underfill(grid, value, patch):
    (h, w) = (len(grid), len(grid[0]))
    bg = mostcolor(grid)
    g = list((list(r) for r in grid))
    for (i, j) in toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            if g[i][j] == bg:
                g[i][j] = value
    return tuple((tuple(r) for r in g))

def hconcat(a, b):
    return tuple((i + j for (i, j) in zip(a, b)))

def vconcat(a, b):
    return a + b

def index(grid, loc):
    (i, j) = loc
    (h, w) = (len(grid), len(grid[0]))
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]]

def p(g):
    return [list(v) for v in solve_10fcaaa3(tuple((tuple(r) for r in g)))]

def solve_10fcaaa3(I):
    x1 = leastcolor(I)
    x2 = hconcat(I, I)
    x3 = vconcat(x2, x2)
    x4 = ofcolor(x3, x1)
    x5 = mapply(ineighbors, x4)
    O = underfill(x3, 8, x5)
    return O