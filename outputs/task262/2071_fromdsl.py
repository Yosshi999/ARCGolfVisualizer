def merge(containers):
    return type(containers)((e for c in containers for e in c))

def sfilter(container, condition):
    return type(container)((e for e in container if condition(e)))

def last(container):
    return max(enumerate(container))[1]

def chain(h, g, f):
    return lambda x: h(g(f(x)))

def matcher(function, target):
    return lambda x: function(x) == target

def lbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda y: function(fixed, y)
    elif n == 3:
        return lambda y, z: function(fixed, y, z)
    else:
        return lambda y, z, a: function(fixed, y, z, a)

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

def hfrontier(location):
    return frozenset(((location[0], j) for j in range(30)))

def p(g):
    return [list(v) for v in solve_a85d4709(tuple((tuple(r) for r in g)))]

def solve_a85d4709(I):
    x1 = ofcolor(I, 5)
    x2 = lbind(matcher, last)
    x3 = lbind(sfilter, x1)
    x4 = lbind(mapply, hfrontier)
    x5 = chain(x4, x3, x2)
    x6 = x5(0)
    x7 = x5(2)
    x8 = x5(1)
    x9 = fill(I, 2, x6)
    x10 = fill(x9, 3, x7)
    O = fill(x10, 4, x8)
    return O