def identity(x):
    return x

def merge(containers):
    return type(containers)((e for c in containers for e in c))

def remove(value, container):
    return type(container)((e for e in container if e != value))

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

def fork(outer, a, b):
    return lambda x: outer(a(x), b(x))

def apply(function, container):
    return type(container)((function(e) for e in container))

def mapply(function, container):
    return merge(apply(function, container))

def prapply(function, a, b):
    return frozenset((function(i, j) for j in b for i in a))

def ofcolor(grid, value):
    return frozenset(((i, j) for (i, r) in enumerate(grid) for (j, v) in enumerate(r) if v == value))

def toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((index for (value, index) in patch))
    return patch

def recolor(value, patch):
    return frozenset(((value, index) for index in toindices(patch)))

def palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for (v, _) in element})

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

def connect(a, b):
    (ai, aj) = a
    (bi, bj) = b
    si = min(ai, bi)
    ei = max(ai, bi) + 1
    sj = min(aj, bj)
    ej = max(aj, bj) + 1
    if ai == bi:
        return frozenset(((ai, j) for j in range(sj, ej)))
    elif aj == bj:
        return frozenset(((i, aj) for i in range(si, ei)))
    elif bi - ai == bj - aj:
        return frozenset(((i, j) for (i, j) in zip(range(si, ei), range(sj, ej))))
    elif bi - ai == aj - bj:
        return frozenset(((i, j) for (i, j) in zip(range(si, ei), range(ej - 1, sj - 1, -1))))
    return frozenset()

def p(g):
    return [list(v) for v in solve_22168020(tuple((tuple(r) for r in g)))]

def solve_22168020(I):
    x1 = palette(I)
    x2 = remove(0, x1)
    x3 = lbind(ofcolor, I)
    x4 = lbind(prapply, connect)
    x5 = fork(x4, x3, x3)
    x6 = compose(merge, x5)
    x7 = fork(recolor, identity, x6)
    x8 = mapply(x7, x2)
    O = paint(I, x8)
    return O