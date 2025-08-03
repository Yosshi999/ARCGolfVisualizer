def size(container):
    return len(container)

def merge(containers):
    return type(containers)((e for c in containers for e in c))

def argmax(container, compfunc):
    return max(container, key=compfunc)

def interval(start, stop, step):
    return tuple(range(start, stop, step))

def astuple(a, b):
    return (a, b)

def chain(h, g, f):
    return lambda x: h(g(f(x)))

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

def prapply(function, a, b):
    return frozenset((function(i, j) for j in b for i in a))

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

def uppermost(patch):
    return min((i for (i, j) in toindices(patch)))

def lowermost(patch):
    return max((i for (i, j) in toindices(patch)))

def leftmost(patch):
    return min((j for (i, j) in toindices(patch)))

def rightmost(patch):
    return max((j for (i, j) in toindices(patch)))

def asobject(grid):
    return frozenset(((v, (i, j)) for (i, r) in enumerate(grid) for (j, v) in enumerate(r)))

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

def canvas(value, dimensions):
    return tuple((tuple((value for j in range(dimensions[1]))) for i in range(dimensions[0])))

def occurrences(grid, obj):
    occs = set()
    normed = normalize(obj)
    (h, w) = (len(grid), len(grid[0]))
    (oh, ow) = shape(obj)
    (h2, w2) = (h - oh + 1, w - ow + 1)
    for i in range(h2):
        for j in range(w2):
            occurs = True
            for (v, (a, b)) in shift(normed, (i, j)):
                if not (0 <= a < h and 0 <= b < w and (grid[a][b] == v)):
                    occurs = False
                    break
            if occurs:
                occs.add((i, j))
    return frozenset(occs)

def p(g):
    return [list(v) for v in solve_3eda0437(tuple((tuple(r) for r in g)))]

def solve_3eda0437(I):
    x1 = interval(2, 10, 1)
    x2 = prapply(astuple, x1, x1)
    x3 = lbind(canvas, 0)
    x4 = lbind(occurrences, I)
    x5 = lbind(lbind, shift)
    x6 = fork(apply, x5, x4)
    x7 = chain(x6, asobject, x3)
    x8 = mapply(x7, x2)
    x9 = argmax(x8, size)
    O = fill(I, 6, x9)
    return O