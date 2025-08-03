def identity(x):
    return x

def flip(b):
    return not b

def contained(value, container):
    return value in container

def size(container):
    return len(container)

def merge(containers):
    return type(containers)((e for c in containers for e in c))

def argmax(container, compfunc):
    return max(container, key=compfunc)

def both(a, b):
    return a and b

def increment(x):
    return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)

def sfilter(container, condition):
    return type(container)((e for e in container if condition(e)))

def first(container):
    return next(iter(container))

def last(container):
    return max(enumerate(container))[1]

def remove(value, container):
    return type(container)((e for e in container if e != value))

def interval(start, stop, step):
    return tuple(range(start, stop, step))

def pair(a, b):
    return tuple(zip(a, b))

def compose(outer, inner):
    return lambda x: outer(inner(x))

def chain(h, g, f):
    return lambda x: h(g(f(x)))

def matcher(function, target):
    return lambda x: function(x) == target

def rbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda x: function(x, fixed)
    elif n == 3:
        return lambda x, y: function(x, y, fixed)
    else:
        return lambda x, y, z: function(x, y, z, fixed)

def lbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda y: function(fixed, y)
    elif n == 3:
        return lambda y, z: function(fixed, y, z)
    else:
        return lambda y, z, a: function(fixed, y, z, a)

def power(function, n):
    if n == 1:
        return function
    return compose(function, power(function, n - 1))

def fork(outer, a, b):
    return lambda x: outer(a(x), b(x))

def apply(function, container):
    return type(container)((function(e) for e in container))

def mapply(function, container):
    return merge(apply(function, container))

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

def urcorner(patch):
    return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))

def llcorner(patch):
    return tuple(map(lambda ix: {0: max, 1: min}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))

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

def recolor(value, patch):
    return frozenset(((value, index) for index in toindices(patch)))

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

def fgpartition(grid):
    return frozenset((frozenset(((v, (i, j)) for (i, r) in enumerate(grid) for (j, v) in enumerate(r) if v == value)) for value in palette(grid) - {mostcolor(grid)}))

def uppermost(patch):
    return min((i for (i, j) in toindices(patch)))

def lowermost(patch):
    return max((i for (i, j) in toindices(patch)))

def leftmost(patch):
    return min((j for (i, j) in toindices(patch)))

def rightmost(patch):
    return max((j for (i, j) in toindices(patch)))

def palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for (v, _) in element})

def numcolors(element):
    return len(palette(element))

def color(obj):
    return next(iter(obj))[0]

def toobject(patch, grid):
    (h, w) = (len(grid), len(grid[0]))
    return frozenset(((grid[i][j], (i, j)) for (i, j) in toindices(patch) if 0 <= i < h and 0 <= j < w))

def dmirror(piece):
    if isinstance(piece, tuple):
        return tuple(zip(*piece))
    (a, b) = ulcorner(piece)
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset(((v, (j - b + a, i - a + b)) for (v, (i, j)) in piece))
    return frozenset(((j - b + a, i - a + b) for (i, j) in piece))

def paint(grid, obj):
    (h, w) = (len(grid), len(grid[0]))
    grid_painted = list((list(row) for row in grid))
    for (value, (i, j)) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_painted[i][j] = value
    return tuple((tuple(row) for row in grid_painted))

def downscale(grid, factor):
    (h, w) = (len(grid), len(grid[0]))
    g = tuple()
    for i in range(h):
        r = tuple()
        for j in range(w):
            if j % factor == 0:
                r = r + (grid[i][j],)
        g = g + (r,)
    h = len(g)
    dsg = tuple()
    for i in range(h):
        if i % factor == 0:
            dsg = dsg + (g[i],)
    return dsg

def subgrid(patch, grid):
    return crop(grid, ulcorner(patch), shape(patch))

def index(grid, loc):
    (i, j) = loc
    (h, w) = (len(grid), len(grid[0]))
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]]

def corners(patch):
    return frozenset({ulcorner(patch), urcorner(patch), llcorner(patch), lrcorner(patch)})

def outbox(patch):
    (ai, aj) = (uppermost(patch) - 1, leftmost(patch) - 1)
    (bi, bj) = (lowermost(patch) + 1, rightmost(patch) + 1)
    (si, sj) = (min(ai, bi), min(aj, bj))
    (ei, ej) = (max(ai, bi), max(aj, bj))
    vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
    hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
    return frozenset(vlines | hlines)

def frontiers(grid):
    (h, w) = (len(grid), len(grid[0]))
    row_indices = tuple((i for (i, r) in enumerate(grid) if len(set(r)) == 1))
    column_indices = tuple((j for (j, c) in enumerate(dmirror(grid)) if len(set(c)) == 1))
    hfrontiers = frozenset({frozenset({(grid[i][j], (i, j)) for j in range(w)}) for i in row_indices})
    vfrontiers = frozenset({frozenset({(grid[i][j], (i, j)) for i in range(h)}) for j in column_indices})
    return hfrontiers | vfrontiers

def p(g):
    return [list(v) for v in solve_7837ac64(tuple((tuple(r) for r in g)))]

def solve_7837ac64(I):
    x1 = fgpartition(I)
    x2 = argmax(x1, size)
    x3 = remove(x2, x1)
    x4 = merge(x3)
    x5 = subgrid(x4, I)
    x6 = chain(color, merge, frontiers)
    x7 = x6(I)
    x8 = objects(x5, True, False, False)
    x9 = colorfilter(x8, 0)
    x10 = rbind(toobject, x5)
    x11 = chain(x10, corners, outbox)
    x12 = lbind(contained, x7)
    x13 = chain(x12, palette, x11)
    x14 = compose(numcolors, x11)
    x15 = compose(flip, x13)
    x16 = matcher(x14, 1)
    x17 = fork(both, x15, x16)
    x18 = sfilter(x9, x17)
    x19 = compose(color, x11)
    x20 = fork(recolor, x19, identity)
    x21 = mapply(x20, x18)
    x22 = paint(x5, x21)
    x23 = first(x9)
    x24 = height(x23)
    x25 = height(x5)
    x26 = increment(x24)
    x27 = interval(0, x25, x26)
    x28 = interval(0, x25, 1)
    x29 = rbind(contained, x27)
    x30 = chain(flip, x29, last)
    x31 = lbind(apply, first)
    x32 = rbind(sfilter, x30)
    x33 = rbind(pair, x28)
    x34 = chain(x31, x32, x33)
    x35 = compose(dmirror, x34)
    x36 = power(x35, 2)
    x37 = x36(x22)
    O = downscale(x37, x24)
    return O