def identity(x):
    return x

def equality(a, b):
    return a == b

def size(container):
    return len(container)

def argmax(container, compfunc):
    return max(container, key=compfunc)

def argmin(container, compfunc):
    return min(container, key=compfunc)

def branch(condition, a, b):
    return a if condition else b

def compose(outer, inner):
    return lambda x: outer(inner(x))

def chain(h, g, f):
    return lambda x: h(g(f(x)))

def power(function, n):
    if n == 1:
        return function
    return compose(function, power(function, n - 1))

def mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for (v, _) in element]
    return max(set(values), key=values.count)

def leastcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for (v, _) in element]
    return min(set(values), key=values.count)

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

def fill(grid, value, patch):
    (h, w) = (len(grid), len(grid[0]))
    grid_filled = list((list(row) for row in grid))
    for (i, j) in toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_filled[i][j] = value
    return tuple((tuple(row) for row in grid_filled))

def replace(grid, replacee, replacer):
    return tuple((tuple((replacer if v == replacee else v for v in r)) for r in grid))

def index(grid, loc):
    (i, j) = loc
    (h, w) = (len(grid), len(grid[0]))
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]]

def outbox(patch):
    (ai, aj) = (uppermost(patch) - 1, leftmost(patch) - 1)
    (bi, bj) = (lowermost(patch) + 1, rightmost(patch) + 1)
    (si, sj) = (min(ai, bi), min(aj, bj))
    (ei, ej) = (max(ai, bi), max(aj, bj))
    vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
    hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
    return frozenset(vlines | hlines)

def p(g):
    return [list(v) for v in solve_f8c80d96(tuple((tuple(r) for r in g)))]

def solve_f8c80d96(I):
    x1 = leastcolor(I)
    x2 = objects(I, True, False, False)
    x3 = colorfilter(x2, x1)
    x4 = argmax(x3, size)
    x5 = argmin(x2, width)
    x6 = size(x5)
    x7 = equality(x6, 1)
    x8 = branch(x7, identity, outbox)
    x9 = chain(outbox, outbox, x8)
    x10 = power(x9, 2)
    x11 = power(x9, 3)
    x12 = x9(x4)
    x13 = x10(x4)
    x14 = x11(x4)
    x15 = fill(I, x1, x12)
    x16 = fill(x15, x1, x13)
    x17 = fill(x16, x1, x14)
    O = replace(x17, 0, 5)
    return O