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

def vmirror(piece):
    if isinstance(piece, tuple):
        return tuple((row[::-1] for row in piece))
    d = ulcorner(piece)[1] + lrcorner(piece)[1]
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset(((v, (i, d - j)) for (v, (i, j)) in piece))
    return frozenset(((i, d - j) for (i, j) in piece))

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
    return [list(v) for v in solve_62c24649(tuple((tuple(r) for r in g)))]

def solve_62c24649(I):
    x1 = vmirror(I)
    x2 = hconcat(I, x1)
    x3 = hmirror(x2)
    O = vconcat(x2, x3)
    return O