NEG_UNITY = (-1, -1)

def merge(containers):
    return type(containers)((e for c in containers for e in c))

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

def leastcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for (v, _) in element]
    return min(set(values), key=values.count)

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

def shift(patch, directions):
    if len(patch) == 0:
        return patch
    (di, dj) = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset(((value, (i + di, j + dj)) for (value, (i, j)) in patch))
    return frozenset(((i + di, j + dj) for (i, j) in patch))

def normalize(patch):
    if len(patch) == 0:
        return patch
    return shift(patch, (-uppermost(patch), -leftmost(patch)))

def uppermost(patch):
    return min((i for (i, j) in toindices(patch)))

def lowermost(patch):
    return max((i for (i, j) in toindices(patch)))

def leftmost(patch):
    return min((j for (i, j) in toindices(patch)))

def rightmost(patch):
    return max((j for (i, j) in toindices(patch)))

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

def inbox(patch):
    (ai, aj) = (uppermost(patch) + 1, leftmost(patch) + 1)
    (bi, bj) = (lowermost(patch) - 1, rightmost(patch) - 1)
    (si, sj) = (min(ai, bi), min(aj, bj))
    (ei, ej) = (max(ai, bi), max(aj, bj))
    vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
    hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
    return frozenset(vlines | hlines)

def occurrences(grid, obj):
    occs = set()
    normed = normalize(obj)
    (h, w) = (len(grid), len(grid[0]))
    (oh, ow) = shape(obj)
    (h2, w2) = (h - oh + 1, w - ow + 1)
    for i in range(h2):
        for j in range(w2):
            occurs = True
            for (v, (a, b)) in shift(normed, (i, j)):
                if not (0 <= a < h and 0 <= b < w and (grid[a][b] == v)):
                    occurs = False
                    break
            if occurs:
                occs.add((i, j))
    return frozenset(occs)

def p(g):
    return [list(v) for v in solve_890034e9(tuple((tuple(r) for r in g)))]

def solve_890034e9(I):
    x1 = leastcolor(I)
    x2 = ofcolor(I, x1)
    x3 = inbox(x2)
    x4 = recolor(0, x3)
    x5 = occurrences(I, x4)
    x6 = normalize(x2)
    x7 = shift(x6, NEG_UNITY)
    x8 = lbind(shift, x7)
    x9 = mapply(x8, x5)
    O = fill(I, x1, x9)
    return O