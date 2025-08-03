UNITY = (1, 1)
NEG_UNITY = (-1, -1)
UP_RIGHT = (-1, 1)
DOWN_LEFT = (1, -1)

def combine(a, b):
    return type(a)((*a, *b))

def size(container):
    return len(container)

def argmax(container, compfunc):
    return max(container, key=compfunc)

def argmin(container, compfunc):
    return min(container, key=compfunc)

def decrement(x):
    return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)

def mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for (v, _) in element]
    return max(set(values), key=values.count)

def asindices(grid):
    return frozenset(((i, j) for i in range(len(grid)) for j in range(len(grid[0]))))

def ulcorner(patch):
    return tuple(map(min, zip(*toindices(patch))))

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

def palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for (v, _) in element})

def numcolors(element):
    return len(palette(element))

def paint(grid, obj):
    (h, w) = (len(grid), len(grid[0]))
    grid_painted = list((list(row) for row in grid))
    for (value, (i, j)) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_painted[i][j] = value
    return tuple((tuple(row) for row in grid_painted))

def underfill(grid, value, patch):
    (h, w) = (len(grid), len(grid[0]))
    bg = mostcolor(grid)
    g = list((list(r) for r in grid))
    for (i, j) in toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            if g[i][j] == bg:
                g[i][j] = value
    return tuple((tuple(r) for r in g))

def upscale(element, factor):
    if isinstance(element, tuple):
        g = tuple()
        for row in element:
            upscaled_row = tuple()
            for value in row:
                upscaled_row = upscaled_row + tuple((value for num in range(factor)))
            g = g + tuple((upscaled_row for num in range(factor)))
        return g
    else:
        if len(element) == 0:
            return frozenset()
        (di_inv, dj_inv) = ulcorner(element)
        (di, dj) = (-di_inv, -dj_inv)
        normed_obj = shift(element, (di, dj))
        o = set()
        for (value, (i, j)) in normed_obj:
            for io in range(factor):
                for jo in range(factor):
                    o.add((value, (i * factor + io, j * factor + jo)))
        return shift(frozenset(o), (di_inv, dj_inv))

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

def shoot(start, direction):
    return connect(start, (start[0] + 42 * direction[0], start[1] + 42 * direction[1]))

def p(g):
    return [list(v) for v in solve_469497ad(tuple((tuple(r) for r in g)))]

def solve_469497ad(I):
    x1 = numcolors(I)
    x2 = decrement(x1)
    x3 = upscale(I, x2)
    x4 = objects(x3, False, False, True)
    x5 = argmin(x4, size)
    x6 = ulcorner(x5)
    x7 = llcorner(x5)
    x8 = shoot(x6, NEG_UNITY)
    x9 = shoot(x6, UNITY)
    x10 = shoot(x7, DOWN_LEFT)
    x11 = shoot(x7, UP_RIGHT)
    x12 = combine(x8, x9)
    x13 = combine(x10, x11)
    x14 = combine(x12, x13)
    x15 = underfill(x3, 2, x14)
    x16 = objects(x15, True, False, True)
    x17 = argmax(x16, lrcorner)
    O = paint(x15, x17)
    return O