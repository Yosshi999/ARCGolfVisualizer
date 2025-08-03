ORIGIN = (0, 0)
TWO_BY_ZERO = (2, 0)
THREE_BY_THREE = (3, 3)

def combine(a, b):
    return type(a)((*a, *b))

def merge(containers):
    return type(containers)((e for c in containers for e in c))

def tojvec(j):
    return (0, j)

def astuple(a, b):
    return (a, b)

def rbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda x: function(x, fixed)
    elif n == 3:
        return lambda x, y: function(x, y, fixed)
    else:
        return lambda x, y, z: function(x, y, z, fixed)

def apply(function, container):
    return type(container)((function(e) for e in container))

def mapply(function, container):
    return merge(apply(function, container))

def leastcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for (v, _) in element]
    return min(set(values), key=values.count)

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

def index(grid, loc):
    (i, j) = loc
    (h, w) = (len(grid), len(grid[0]))
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]]

def canvas(value, dimensions):
    return tuple((tuple((value for j in range(dimensions[1]))) for i in range(dimensions[0])))

def p(g):
    return [list(v) for v in solve_bc1d5164(tuple((tuple(r) for r in g)))]

def solve_bc1d5164(I):
    x1 = leastcolor(I)
    x2 = crop(I, ORIGIN, THREE_BY_THREE)
    x3 = crop(I, TWO_BY_ZERO, THREE_BY_THREE)
    x4 = tojvec(4)
    x5 = crop(I, x4, THREE_BY_THREE)
    x6 = astuple(2, 4)
    x7 = crop(I, x6, THREE_BY_THREE)
    x8 = canvas(0, THREE_BY_THREE)
    x9 = rbind(ofcolor, x1)
    x10 = astuple(x2, x3)
    x11 = astuple(x5, x7)
    x12 = combine(x10, x11)
    x13 = mapply(x9, x12)
    O = fill(x8, x1, x13)
    return O