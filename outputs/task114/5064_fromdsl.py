UNITY = (1, 1)

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

def difference(a, b):
    return type(a)((e for e in a if e not in b))

def argmin(container, compfunc):
    return min(container, key=compfunc)

def initset(value):
    return frozenset({value})

def first(container):
    return next(iter(container))

def astuple(a, b):
    return (a, b)

def compose(outer, inner):
    return lambda x: outer(inner(x))

def chain(h, g, f):
    return lambda x: h(g(f(x)))

def rbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda x: function(x, fixed)
    elif n == 3:
        return lambda x, y: function(x, y, fixed)
    else:
        return lambda x, y, z: function(x, y, z, fixed)

def lbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda y: function(fixed, y)
    elif n == 3:
        return lambda y, z: function(fixed, y, z)
    else:
        return lambda y, z, a: function(fixed, y, z, a)

def fork(outer, a, b):
    return lambda x: outer(a(x), b(x))

def apply(function, container):
    return type(container)((function(e) for e in container))

def height(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece)
    return lowermost(piece) - uppermost(piece) + 1

def width(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece[0])
    return rightmost(piece) - leftmost(piece) + 1

def shape(piece):
    return (height(piece), width(piece))

def asindices(grid):
    return frozenset(((i, j) for i in range(len(grid)) for j in range(len(grid[0]))))

def ulcorner(patch):
    return tuple(map(min, zip(*toindices(patch))))

def urcorner(patch):
    return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))

def llcorner(patch):
    return tuple(map(lambda ix: {0: max, 1: min}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))

def lrcorner(patch):
    return tuple(map(max, zip(*toindices(patch))))

def toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((index for (value, index) in patch))
    return patch

def shift(patch, directions):
    if len(patch) == 0:
        return patch
    (di, dj) = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset(((value, (i + di, j + dj)) for (value, (i, j)) in patch))
    return frozenset(((i + di, j + dj) for (i, j) in patch))

def uppermost(patch):
    return min((i for (i, j) in toindices(patch)))

def lowermost(patch):
    return max((i for (i, j) in toindices(patch)))

def leftmost(patch):
    return min((j for (i, j) in toindices(patch)))

def rightmost(patch):
    return max((j for (i, j) in toindices(patch)))

def manhattan(a, b):
    return min((abs(ai - bi) + abs(aj - bj) for (ai, aj) in toindices(a) for (bi, bj) in toindices(b)))

def asobject(grid):
    return frozenset(((v, (i, j)) for (i, r) in enumerate(grid) for (j, v) in enumerate(r)))

def paint(grid, obj):
    (h, w) = (len(grid), len(grid[0]))
    grid_painted = list((list(row) for row in grid))
    for (value, (i, j)) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_painted[i][j] = value
    return tuple((tuple(row) for row in grid_painted))

def index(grid, loc):
    (i, j) = loc
    (h, w) = (len(grid), len(grid[0]))
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]]

def canvas(value, dimensions):
    return tuple((tuple((value for j in range(dimensions[1]))) for i in range(dimensions[0])))

def corners(patch):
    return frozenset({ulcorner(patch), urcorner(patch), llcorner(patch), lrcorner(patch)})

def box(patch):
    if len(patch) == 0:
        return patch
    (ai, aj) = ulcorner(patch)
    (bi, bj) = lrcorner(patch)
    (si, sj) = (min(ai, bi), min(aj, bj))
    (ei, ej) = (max(ai, bi), max(aj, bj))
    vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
    hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
    return frozenset(vlines | hlines)

def p(g):
    return [list(v) for v in solve_49d1d64f(tuple((tuple(r) for r in g)))]

def solve_49d1d64f(I):
    x1 = shape(I)
    x2 = add(x1, 2)
    x3 = canvas(0, x2)
    x4 = asobject(I)
    x5 = shift(x4, UNITY)
    x6 = paint(x3, x5)
    x7 = asindices(x3)
    x8 = fork(difference, box, corners)
    x9 = x8(x7)
    x10 = lbind(lbind, manhattan)
    x11 = rbind(compose, initset)
    x12 = chain(x11, x10, initset)
    x13 = lbind(argmin, x5)
    x14 = chain(first, x13, x12)
    x15 = fork(astuple, x14, identity)
    x16 = apply(x15, x9)
    O = paint(x6, x16)
    return O