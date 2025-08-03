def identity(x):
    return x

def equality(a, b):
    return a == b

def dedupe(tup):
    return tuple((e for (i, e) in enumerate(tup) if tup.index(e) == i))

def order(container, compfunc):
    return tuple(sorted(container, key=compfunc))

def repeat(item, num):
    return tuple((item for i in range(num)))

def size(container):
    return len(container)

def first(container):
    return next(iter(container))

def branch(condition, a, b):
    return a if condition else b

def chain(h, g, f):
    return lambda x: h(g(f(x)))

def apply(function, container):
    return type(container)((function(e) for e in container))

def mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for (v, _) in element]
    return max(set(values), key=values.count)

def asindices(grid):
    return frozenset(((i, j) for i in range(len(grid)) for j in range(len(grid[0]))))

def ulcorner(patch):
    return tuple(map(min, zip(*toindices(patch))))

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

def leftmost(patch):
    return min((j for (i, j) in toindices(patch)))

def color(obj):
    return next(iter(obj))[0]

def dmirror(piece):
    if isinstance(piece, tuple):
        return tuple(zip(*piece))
    (a, b) = ulcorner(piece)
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset(((v, (j - b + a, i - a + b)) for (v, (i, j)) in piece))
    return frozenset(((j - b + a, i - a + b) for (i, j) in piece))

def index(grid, loc):
    (i, j) = loc
    (h, w) = (len(grid), len(grid[0]))
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]]

def p(g):
    return [list(v) for v in solve_746b3537(tuple((tuple(r) for r in g)))]

def solve_746b3537(I):
    x1 = chain(size, dedupe, first)
    x2 = x1(I)
    x3 = equality(x2, 1)
    x4 = branch(x3, dmirror, identity)
    x5 = x4(I)
    x6 = objects(x5, True, False, False)
    x7 = order(x6, leftmost)
    x8 = apply(color, x7)
    x9 = repeat(x8, 1)
    O = x4(x9)
    return O