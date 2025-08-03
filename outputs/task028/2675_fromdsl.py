TWO_BY_ZERO = (2, 0)

def combine(a, b):
    return type(a)((*a, *b))

def leastcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for (v, _) in element]
    return min(set(values), key=values.count)

def asindices(grid):
    return frozenset(((i, j) for i in range(len(grid)) for j in range(len(grid[0]))))

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

def fill(grid, value, patch):
    (h, w) = (len(grid), len(grid[0]))
    grid_filled = list((list(row) for row in grid))
    for (i, j) in toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_filled[i][j] = value
    return tuple((tuple(row) for row in grid_filled))

def vconcat(a, b):
    return a + b

def replace(grid, replacee, replacer):
    return tuple((tuple((replacer if v == replacee else v for v in r)) for r in grid))

def index(grid, loc):
    (i, j) = loc
    (h, w) = (len(grid), len(grid[0]))
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]]

def tophalf(grid):
    return grid[:len(grid) // 2]

def bottomhalf(grid):
    return grid[len(grid) // 2 + len(grid) % 2:]

def hfrontier(location):
    return frozenset(((location[0], j) for j in range(30)))

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
    return [list(v) for v in solve_1bfc4729(tuple((tuple(r) for r in g)))]

def solve_1bfc4729(I):
    x1 = asindices(I)
    x2 = tophalf(I)
    x3 = bottomhalf(I)
    x4 = leastcolor(x2)
    x5 = leastcolor(x3)
    x6 = hfrontier(TWO_BY_ZERO)
    x7 = box(x1)
    x8 = combine(x6, x7)
    x9 = fill(x2, x4, x8)
    x10 = hmirror(x9)
    x11 = replace(x10, x4, x5)
    O = vconcat(x9, x11)
    return O