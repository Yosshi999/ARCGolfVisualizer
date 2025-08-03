def flip(b):
    return not b

def equality(a, b):
    return a == b

def merge(containers):
    return type(containers)((e for c in containers for e in c))

def sfilter(container, condition):
    return type(container)((e for e in container if condition(e)))

def mfilter(container, function):
    return merge(sfilter(container, function))

def extract(container, condition):
    return next((e for e in container if condition(e)))

def first(container):
    return next(iter(container))

def compose(outer, inner):
    return lambda x: outer(inner(x))

def matcher(function, target):
    return lambda x: function(x) == target

def fork(outer, a, b):
    return lambda x: outer(a(x), b(x))

def mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for (v, _) in element]
    return max(set(values), key=values.count)

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

def colorfilter(objs, value):
    return frozenset((obj for obj in objs if next(iter(obj))[0] == value))

def asindices(grid):
    return frozenset(((i, j) for i in range(len(grid)) for j in range(len(grid[0]))))

def ulcorner(patch):
    return tuple(map(min, zip(*toindices(patch))))

def lrcorner(patch):
    return tuple(map(max, zip(*toindices(patch))))

def crop(grid, start, dims):
    return tuple((r[start[1]:start[1] + dims[1]] for r in grid[start[0]:start[0] + dims[0]]))

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

def normalize(patch):
    if len(patch) == 0:
        return patch
    return shift(patch, (-uppermost(patch), -leftmost(patch)))

def dneighbors(loc):
    return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})

def ineighbors(loc):
    return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})

def neighbors(loc):
    return dneighbors(loc) | ineighbors(loc)

def objects(grid, univalued, diagonal, without_bg):
    bg = mostcolor(grid) if without_bg else None
    objs = set()
    occupied = set()
    (h, w) = (len(grid), len(grid[0]))
    unvisited = asindices(grid)
    diagfun = neighbors if diagonal else dneighbors
    for loc in unvisited:
        if loc in occupied:
            continue
        val = grid[loc[0]][loc[1]]
        if val == bg:
            continue
        obj = {(val, loc)}
        cands = {loc}
        while len(cands) > 0:
            neighborhood = set()
            for cand in cands:
                v = grid[cand[0]][cand[1]]
                if val == v if univalued else v != bg:
                    obj.add((v, cand))
                    occupied.add(cand)
                    neighborhood |= {(i, j) for (i, j) in diagfun(cand) if 0 <= i < h and 0 <= j < w}
            cands = neighborhood - occupied
        objs.add(frozenset(obj))
    return frozenset(objs)

def uppermost(patch):
    return min((i for (i, j) in toindices(patch)))

def lowermost(patch):
    return max((i for (i, j) in toindices(patch)))

def leftmost(patch):
    return min((j for (i, j) in toindices(patch)))

def rightmost(patch):
    return max((j for (i, j) in toindices(patch)))

def color(obj):
    return next(iter(obj))[0]

def asobject(grid):
    return frozenset(((v, (i, j)) for (i, r) in enumerate(grid) for (j, v) in enumerate(r)))

def fill(grid, value, patch):
    (h, w) = (len(grid), len(grid[0]))
    grid_filled = list((list(row) for row in grid))
    for (i, j) in toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_filled[i][j] = value
    return tuple((tuple(row) for row in grid_filled))

def subgrid(patch, grid):
    return crop(grid, ulcorner(patch), shape(patch))

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
    return [list(v) for v in solve_776ffc46(tuple((tuple(r) for r in g)))]

def solve_776ffc46(I):
    x1 = objects(I, True, False, True)
    x2 = colorfilter(x1, 5)
    x3 = fork(equality, toindices, box)
    x4 = extract(x2, x3)
    x5 = inbox(x4)
    x6 = subgrid(x5, I)
    x7 = asobject(x6)
    x8 = matcher(first, 0)
    x9 = compose(flip, x8)
    x10 = sfilter(x7, x9)
    x11 = normalize(x10)
    x12 = toindices(x11)
    x13 = compose(toindices, normalize)
    x14 = matcher(x13, x12)
    x15 = mfilter(x1, x14)
    x16 = color(x11)
    O = fill(I, x16, x15)
    return O