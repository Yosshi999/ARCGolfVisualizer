def identity(x):
    return x

def dedupe(tup):
    return tuple((e for (i, e) in enumerate(tup) if tup.index(e) == i))

def last(container):
    return max(enumerate(container))[1]

def remove(value, container):
    return type(container)((e for e in container if e != value))

def compose(outer, inner):
    return lambda x: outer(inner(x))

def fork(outer, a, b):
    return lambda x: outer(a(x), b(x))

def ulcorner(patch):
    return tuple(map(min, zip(*toindices(patch))))

def lrcorner(patch):
    return tuple(map(max, zip(*toindices(patch))))

def toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((index for (value, index) in patch))
    return patch

def hmirror(piece):
    if isinstance(piece, tuple):
        return piece[::-1]
    d = ulcorner(piece)[0] + lrcorner(piece)[0]
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset(((v, (d - i, j)) for (v, (i, j)) in piece))
    return frozenset(((d - i, j) for (i, j) in piece))

def dmirror(piece):
    if isinstance(piece, tuple):
        return tuple(zip(*piece))
    (a, b) = ulcorner(piece)
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset(((v, (j - b + a, i - a + b)) for (v, (i, j)) in piece))
    return frozenset(((j - b + a, i - a + b) for (i, j) in piece))

def vconcat(a, b):
    return a + b

def index(grid, loc):
    (i, j) = loc
    (h, w) = (len(grid), len(grid[0]))
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]]

def p(g):
    return [list(v) for v in solve_eb5a1d5d(tuple((tuple(r) for r in g)))]

def solve_eb5a1d5d(I):
    x1 = compose(dmirror, dedupe)
    x2 = x1(I)
    x3 = x1(x2)
    x4 = fork(remove, last, identity)
    x5 = compose(hmirror, x4)
    x6 = fork(vconcat, identity, x5)
    x7 = x6(x3)
    x8 = dmirror(x7)
    O = x6(x8)
    return O