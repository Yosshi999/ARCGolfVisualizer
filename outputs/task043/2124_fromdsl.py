def first(container):
    return next(iter(container))

def last(container):
    return max(enumerate(container))[1]

def remove(value, container):
    return type(container)((e for e in container if e != value))

def astuple(a, b):
    return (a, b)

def product(a, b):
    return frozenset(((i, j) for j in b for i in a))

def compose(outer, inner):
    return lambda x: outer(inner(x))

def power(function, n):
    if n == 1:
        return function
    return compose(function, power(function, n - 1))

def fork(outer, a, b):
    return lambda x: outer(a(x), b(x))

def apply(function, container):
    return type(container)((function(e) for e in container))

def mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for (v, _) in element]
    return max(set(values), key=values.count)

def ofcolor(grid, value):
    return frozenset(((i, j) for (i, r) in enumerate(grid) for (j, v) in enumerate(r) if v == value))

def urcorner(patch):
    return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))

def toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((index for (value, index) in patch))
    return patch

def underfill(grid, value, patch):
    (h, w) = (len(grid), len(grid[0]))
    bg = mostcolor(grid)
    g = list((list(r) for r in grid))
    for (i, j) in toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            if g[i][j] == bg:
                g[i][j] = value
    return tuple((tuple(r) for r in g))

def index(grid, loc):
    (i, j) = loc
    (h, w) = (len(grid), len(grid[0]))
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]]

def p(g):
    return [list(v) for v in solve_2281f1f4(tuple((tuple(r) for r in g)))]

def solve_2281f1f4(I):
    x1 = ofcolor(I, 5)
    x2 = product(x1, x1)
    x3 = power(first, 2)
    x4 = power(last, 2)
    x5 = fork(astuple, x3, x4)
    x6 = apply(x5, x2)
    x7 = urcorner(x1)
    x8 = remove(x7, x6)
    O = underfill(I, 2, x8)
    return O