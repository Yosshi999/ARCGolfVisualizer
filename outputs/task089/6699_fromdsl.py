def identity(x):
    return x

def invert(n):
    return -n if isinstance(n, int) else (-n[0], -n[1])

def contained(value, container):
    return value in container

def combine(a, b):
    return type(a)((*a, *b))

def size(container):
    return len(container)

def merge(containers):
    return type(containers)((e for c in containers for e in c))

def argmax(container, compfunc):
    return max(container, key=compfunc)

def initset(value):
    return frozenset({value})

def sfilter(container, condition):
    return type(container)((e for e in container if condition(e)))

def insert(value, container):
    return container.union(frozenset({value}))

def remove(value, container):
    return type(container)((e for e in container if e != value))

def astuple(a, b):
    return (a, b)

def compose(outer, inner):
    return lambda x: outer(inner(x))

def chain(h, g, f):
    return lambda x: h(g(f(x)))

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

def vmirror(piece):
    if isinstance(piece, tuple):
        return tuple((row[::-1] for row in piece))
    d = ulcorner(piece)[1] + lrcorner(piece)[1]
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset(((v, (i, d - j)) for (v, (i, j)) in piece))
    return frozenset(((i, d - j) for (i, j) in piece))

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
    return [list(v) for v in solve_3e980e27(tuple((tuple(r) for r in g)))]

def solve_3e980e27(I):
    x1 = objects(I, False, True, True)
    x2 = astuple(10, 10)
    x3 = invert(x2)
    x4 = astuple(2, x3)
    x5 = astuple(3, x3)
    x6 = initset(x4)
    x7 = insert(x5, x6)
    x8 = insert(x7, x1)
    x9 = lbind(contained, 2)
    x10 = lbind(contained, 3)
    x11 = compose(invert, ulcorner)
    x12 = lbind(compose, x11)
    x13 = lbind(rbind, sfilter)
    x14 = compose(x12, x13)
    x15 = rbind(compose, center)
    x16 = lbind(lbind, shift)
    x17 = x14(x9)
    x18 = x14(x10)
    x19 = fork(shift, identity, x17)
    x20 = fork(shift, identity, x18)
    x21 = compose(x9, palette)
    x22 = compose(x10, palette)
    x23 = sfilter(x8, x21)
    x24 = argmax(x23, size)
    x25 = remove(x24, x23)
    x26 = vmirror(x24)
    x27 = chain(x15, x16, x19)
    x28 = x27(x26)
    x29 = mapply(x28, x25)
    x30 = sfilter(x8, x22)
    x31 = argmax(x30, size)
    x32 = remove(x31, x30)
    x33 = chain(x15, x16, x20)
    x34 = x33(x31)
    x35 = mapply(x34, x32)
    x36 = combine(x29, x35)
    O = paint(I, x36)
    return O