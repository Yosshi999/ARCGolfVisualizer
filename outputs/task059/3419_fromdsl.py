def identity(x):
    return x

def add(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] + b[0], a[1] + b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a + b[0], a + b[1])
    return (a[0] + b, a[1] + b)

def flip(b):
    return not b

def merge(containers):
    return type(containers)((e for c in containers for e in c))

def valmax(container, compfunc):
    return compfunc(max(container, key=compfunc, default=0))

def sfilter(container, condition):
    return type(container)((e for e in container if condition(e)))

def mfilter(container, function):
    return merge(sfilter(container, function))

def first(container):
    return next(iter(container))

def last(container):
    return max(enumerate(container))[1]

def interval(start, stop, step):
    return tuple(range(start, stop, step))

def product(a, b):
    return frozenset(((i, j) for j in b for i in a))

def compose(outer, inner):
    return lambda x: outer(inner(x))

def matcher(function, target):
    return lambda x: function(x) == target

def rbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda x: function(x, fixed)
    elif n == 3:
        return lambda x, y: function(x, y, fixed)
    else:
        return lambda x, y, z: function(x, y, z, fixed)

def fork(outer, a, b):
    return lambda x: outer(a(x), b(x))

def apply(function, container):
    return type(container)((function(e) for e in container))

def leastcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for (v, _) in element]
    return min(set(values), key=values.count)

def colorcount(element, value):
    if isinstance(element, tuple):
        return sum((row.count(value) for row in element))
    return sum((v == value for (v, _) in element))

def toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((index for (value, index) in patch))
    return patch

def toobject(patch, grid):
    (h, w) = (len(grid), len(grid[0]))
    return frozenset(((grid[i][j], (i, j)) for (i, j) in toindices(patch) if 0 <= i < h and 0 <= j < w))

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

def p(g):
    return [list(v) for v in solve_29623171(tuple((tuple(r) for r in g)))]

def solve_29623171(I):
    x1 = leastcolor(I)
    x2 = interval(0, 9, 4)
    x3 = product(x2, x2)
    x4 = rbind(add, 3)
    x5 = rbind(interval, 1)
    x6 = fork(x5, identity, x4)
    x7 = compose(x6, first)
    x8 = compose(x6, last)
    x9 = fork(product, x7, x8)
    x10 = rbind(colorcount, x1)
    x11 = rbind(toobject, I)
    x12 = compose(x10, x11)
    x13 = apply(x9, x3)
    x14 = valmax(x13, x12)
    x15 = matcher(x12, x14)
    x16 = compose(flip, x15)
    x17 = mfilter(x13, x15)
    x18 = mfilter(x13, x16)
    x19 = fill(I, x1, x17)
    O = fill(x19, 0, x18)
    return O