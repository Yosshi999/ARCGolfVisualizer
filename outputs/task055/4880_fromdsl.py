def flip(b):
    return not b

def argmax(container, compfunc):
    return max(container, key=compfunc)

def argmin(container, compfunc):
    return min(container, key=compfunc)

def sfilter(container, condition):
    return type(container)((e for e in container if condition(e)))

def extract(container, condition):
    return next((e for e in container if condition(e)))

def remove(value, container):
    return type(container)((e for e in container if e != value))

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

def lbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda y: function(fixed, y)
    elif n == 3:
        return lambda y, z: function(fixed, y, z)
    else:
        return lambda y, z, a: function(fixed, y, z, a)

def apply(function, container):
    return type(container)((function(e) for e in container))

def mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for (v, _) in element]
    return max(set(values), key=values.count)

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

def hmatching(a, b):
    return len(set((i for (i, j) in toindices(a))) & set((i for (i, j) in toindices(b)))) > 0

def vmatching(a, b):
    return len(set((j for (i, j) in toindices(a))) & set((j for (i, j) in toindices(b)))) > 0

def bordering(patch, grid):
    return uppermost(patch) == 0 or leftmost(patch) == 0 or lowermost(patch) == len(grid) - 1 or (rightmost(patch) == len(grid[0]) - 1)

def fill(grid, value, patch):
    (h, w) = (len(grid), len(grid[0]))
    grid_filled = list((list(row) for row in grid))
    for (i, j) in toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_filled[i][j] = value
    return tuple((tuple(row) for row in grid_filled))

def index(grid, loc):
    (i, j) = loc
    (h, w) = (len(grid), len(grid[0]))
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]]

def p(g):
    return [list(v) for v in solve_272f95fa(tuple((tuple(r) for r in g)))]

def solve_272f95fa(I):
    x1 = objects(I, True, False, False)
    x2 = colorfilter(x1, 0)
    x3 = apply(toindices, x2)
    x4 = rbind(bordering, I)
    x5 = compose(flip, x4)
    x6 = extract(x3, x5)
    x7 = remove(x6, x3)
    x8 = lbind(vmatching, x6)
    x9 = lbind(hmatching, x6)
    x10 = sfilter(x7, x8)
    x11 = sfilter(x7, x9)
    x12 = argmin(x10, uppermost)
    x13 = argmax(x10, uppermost)
    x14 = argmin(x11, leftmost)
    x15 = argmax(x11, leftmost)
    x16 = fill(I, 6, x6)
    x17 = fill(x16, 2, x12)
    x18 = fill(x17, 1, x13)
    x19 = fill(x18, 4, x14)
    O = fill(x19, 3, x15)
    return O