UNITY = (1, 1)

def equality(a, b):
    return a == b

def branch(condition, a, b):
    return a if condition else b

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

def vmirror(piece):
    if isinstance(piece, tuple):
        return tuple((row[::-1] for row in piece))
    d = ulcorner(piece)[1] + lrcorner(piece)[1]
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset(((v, (i, d - j)) for (v, (i, j)) in piece))
    return frozenset(((i, d - j) for (i, j) in piece))

def index(grid, loc):
    (i, j) = loc
    (h, w) = (len(grid), len(grid[0]))
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]]

def canvas(value, dimensions):
    return tuple((tuple((value for j in range(dimensions[1]))) for i in range(dimensions[0])))

def p(g):
    return [list(v) for v in solve_44f52bb0(tuple((tuple(r) for r in g)))]

def solve_44f52bb0(I):
    x1 = vmirror(I)
    x2 = equality(x1, I)
    x3 = branch(x2, 1, 7)
    O = canvas(x3, UNITY)
    return O