ORIGIN = (0, 0)
THREE_BY_THREE = (3, 3)

def merge(containers):
    return type(containers)((e for c in containers for e in c))

def tojvec(j):
    return (0, j)

def astuple(a, b):
    return (a, b)

def apply(function, container):
    return type(container)((function(e) for e in container))

def papply(function, a, b):
    return tuple((function(i, j) for (i, j) in zip(a, b)))

def mpapply(function, a, b):
    return merge(papply(function, a, b))

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

def rot90(grid):
    return tuple((row for row in zip(*grid[::-1])))

def rot180(grid):
    return tuple((tuple(row[::-1]) for row in grid[::-1]))

def paint(grid, obj):
    (h, w) = (len(grid), len(grid[0]))
    grid_painted = list((list(row) for row in grid))
    for (value, (i, j)) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_painted[i][j] = value
    return tuple((tuple(row) for row in grid_painted))

def p(g):
    return [list(v) for v in solve_8e5a5113(tuple((tuple(r) for r in g)))]

def solve_8e5a5113(I):
    x1 = crop(I, ORIGIN, THREE_BY_THREE)
    x2 = rot90(x1)
    x3 = rot180(x1)
    x4 = astuple(x2, x3)
    x5 = astuple(4, 8)
    x6 = apply(tojvec, x5)
    x7 = apply(asobject, x4)
    x8 = mpapply(shift, x7, x6)
    O = paint(I, x8)
    return O