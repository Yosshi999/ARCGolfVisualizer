ORIGIN = (0, 0)
THREE_BY_THREE = (3, 3)

def merge(containers):
    return type(containers)((e for c in containers for e in c))

def decrement(x):
    return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)

def compose(outer, inner):
    return lambda x: outer(inner(x))

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

def crop(grid, start, dims):
    return tuple((r[start[1]:start[1] + dims[1]] for r in grid[start[0]:start[0] + dims[0]]))

def shift(patch, directions):
    if len(patch) == 0:
        return patch
    (di, dj) = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset(((value, (i + di, j + dj)) for (value, (i, j)) in patch))
    return frozenset(((i + di, j + dj) for (i, j) in patch))

def asobject(grid):
    return frozenset(((v, (i, j)) for (i, r) in enumerate(grid) for (j, v) in enumerate(r)))

def paint(grid, obj):
    (h, w) = (len(grid), len(grid[0]))
    grid_painted = list((list(row) for row in grid))
    for (value, (i, j)) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_painted[i][j] = value
    return tuple((tuple(row) for row in grid_painted))

def p(g):
    return [list(v) for v in solve_363442ee(tuple((tuple(r) for r in g)))]

def solve_363442ee(I):
    x1 = ofcolor(I, 1)
    x2 = crop(I, ORIGIN, THREE_BY_THREE)
    x3 = asobject(x2)
    x4 = lbind(shift, x3)
    x5 = compose(x4, decrement)
    x6 = mapply(x5, x1)
    O = paint(I, x6)
    return O