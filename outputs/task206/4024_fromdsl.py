NEG_UNITY = (-1, -1)

def difference(a, b):
    return type(a)((e for e in a if e not in b))

def first(container):
    return next(iter(container))

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

def colorfilter(objs, value):
    return frozenset((obj for obj in objs if next(iter(obj))[0] == value))

def asindices(grid):
    return frozenset(((i, j) for i in range(len(grid)) for j in range(len(grid[0]))))

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

def paint(grid, obj):
    (h, w) = (len(grid), len(grid[0]))
    grid_painted = list((list(row) for row in grid))
    for (value, (i, j)) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_painted[i][j] = value
    return tuple((tuple(row) for row in grid_painted))

def center(patch):
    return (uppermost(patch) + height(patch) // 2, leftmost(patch) + width(patch) // 2)

def index(grid, loc):
    (i, j) = loc
    (h, w) = (len(grid), len(grid[0]))
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]]

def p(g):
    return [list(v) for v in solve_88a10436(tuple((tuple(r) for r in g)))]

def solve_88a10436(I):
    x1 = objects(I, False, False, True)
    x2 = colorfilter(x1, 5)
    x3 = first(x2)
    x4 = center(x3)
    x5 = difference(x1, x2)
    x6 = first(x5)
    x7 = normalize(x6)
    x8 = shift(x7, x4)
    x9 = shift(x8, NEG_UNITY)
    O = paint(I, x9)
    return O