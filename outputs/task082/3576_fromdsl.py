def merge(containers):
    return type(containers)((e for c in containers for e in c))

def first(container):
    return next(iter(container))

def last(container):
    return max(enumerate(container))[1]

def chain(h, g, f):
    return lambda x: h(g(f(x)))

def fork(outer, a, b):
    return lambda x: outer(a(x), b(x))

def apply(function, container):
    return type(container)((function(e) for e in container))

def mapply(function, container):
    return merge(apply(function, container))

def mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for (v, _) in element]
    return max(set(values), key=values.count)

def asindices(grid):
    return frozenset(((i, j) for i in range(len(grid)) for j in range(len(grid[0]))))

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

def color(obj):
    return next(iter(obj))[0]

def paint(grid, obj):
    (h, w) = (len(grid), len(grid[0]))
    grid_painted = list((list(row) for row in grid))
    for (value, (i, j)) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_painted[i][j] = value
    return tuple((tuple(row) for row in grid_painted))

def vconcat(a, b):
    return a + b

def vsplit(grid, n):
    (h, w) = (len(grid) // n, len(grid[0]))
    offset = len(grid) % n != 0
    return tuple((crop(grid, (h * i + i * offset, 0), (h, w)) for i in range(n)))

def index(grid, loc):
    (i, j) = loc
    (h, w) = (len(grid), len(grid[0]))
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]]

def p(g):
    return [list(v) for v in solve_3ac3eb23(tuple((tuple(r) for r in g)))]

def solve_3ac3eb23(I):
    x1 = objects(I, True, False, True)
    x2 = chain(ineighbors, last, first)
    x3 = fork(recolor, color, x2)
    x4 = mapply(x3, x1)
    x5 = paint(I, x4)
    x6 = vsplit(x5, 3)
    x7 = first(x6)
    x8 = vconcat(x7, x7)
    O = vconcat(x7, x8)
    return O