RIGHT = (0, 1)
DOWN_LEFT = (1, -1)

def add(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] + b[0], a[1] + b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a + b[0], a + b[1])
    return (a[0] + b, a[1] + b)

def order(container, compfunc):
    return tuple(sorted(container, key=compfunc))

def merge(containers):
    return type(containers)((e for c in containers for e in c))

def initset(value):
    return frozenset({value})

def first(container):
    return next(iter(container))

def last(container):
    return max(enumerate(container))[1]

def insert(value, container):
    return container.union(frozenset({value}))

def remove(value, container):
    return type(container)((e for e in container if e != value))

def pair(a, b):
    return tuple(zip(a, b))

def compose(outer, inner):
    return lambda x: outer(inner(x))

def rbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda x: function(x, fixed)
    elif n == 3:
        return lambda x, y: function(x, y, fixed)
    else:
        return lambda x, y, z: function(x, y, z, fixed)

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

def asindices(grid):
    return frozenset(((i, j) for i in range(len(grid)) for j in range(len(grid[0]))))

def lrcorner(patch):
    return tuple(map(max, zip(*toindices(patch))))

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

def paint(grid, obj):
    (h, w) = (len(grid), len(grid[0]))
    grid_painted = list((list(row) for row in grid))
    for (value, (i, j)) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_painted[i][j] = value
    return tuple((tuple(row) for row in grid_painted))

def underpaint(grid, obj):
    (h, w) = (len(grid), len(grid[0]))
    bg = mostcolor(grid)
    g = list((list(r) for r in grid))
    for (value, (i, j)) in obj:
        if 0 <= i < h and 0 <= j < w:
            if g[i][j] == bg:
                g[i][j] = value
    return tuple((tuple(r) for r in g))

def center(patch):
    return (uppermost(patch) + height(patch) // 2, leftmost(patch) + width(patch) // 2)

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
    return [list(v) for v in solve_99fa7670(tuple((tuple(r) for r in g)))]

def solve_99fa7670(I):
    x1 = shape(I)
    x2 = objects(I, True, False, True)
    x3 = rbind(shoot, RIGHT)
    x4 = compose(x3, center)
    x5 = fork(recolor, color, x4)
    x6 = mapply(x5, x2)
    x7 = paint(I, x6)
    x8 = add(x1, DOWN_LEFT)
    x9 = initset(x8)
    x10 = recolor(0, x9)
    x11 = objects(x7, True, False, True)
    x12 = insert(x10, x11)
    x13 = order(x12, uppermost)
    x14 = first(x13)
    x15 = remove(x10, x13)
    x16 = remove(x14, x13)
    x17 = compose(lrcorner, first)
    x18 = compose(lrcorner, last)
    x19 = fork(connect, x17, x18)
    x20 = compose(color, first)
    x21 = fork(recolor, x20, x19)
    x22 = pair(x15, x16)
    x23 = mapply(x21, x22)
    O = underpaint(x7, x23)
    return O