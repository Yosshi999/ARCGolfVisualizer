def contained(value, container):
    return value in container

def order(container, compfunc):
    return tuple(sorted(container, key=compfunc))

def size(container):
    return len(container)

def merge(containers):
    return type(containers)((e for c in containers for e in c))

def sfilter(container, condition):
    return type(container)((e for e in container if condition(e)))

def first(container):
    return next(iter(container))

def last(container):
    return max(enumerate(container))[1]

def interval(start, stop, step):
    return tuple(range(start, stop, step))

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

def center(patch):
    return (uppermost(patch) + height(patch) // 2, leftmost(patch) + width(patch) // 2)

def index(grid, loc):
    (i, j) = loc
    (h, w) = (len(grid), len(grid[0]))
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]]

def p(g):
    return [list(v) for v in solve_7447852a(tuple((tuple(r) for r in g)))]

def solve_7447852a(I):
    x1 = objects(I, True, False, False)
    x2 = colorfilter(x1, 0)
    x3 = compose(last, center)
    x4 = order(x2, x3)
    x5 = size(x4)
    x6 = interval(0, x5, 3)
    x7 = rbind(contained, x6)
    x8 = compose(x7, last)
    x9 = interval(0, x5, 1)
    x10 = pair(x4, x9)
    x11 = sfilter(x10, x8)
    x12 = mapply(first, x11)
    O = fill(I, 4, x12)
    return O