def dedupe(tup):
    return tuple((e for (i, e) in enumerate(tup) if tup.index(e) == i))

def repeat(item, num):
    return tuple((item for i in range(num)))

def greater(a, b):
    return a > b

def size(container):
    return len(container)

def mostcommon(container):
    return max(set(container), key=container.count)

def branch(condition, a, b):
    return a if condition else b

def compose(outer, inner):
    return lambda x: outer(inner(x))

def apply(function, container):
    return type(container)((function(e) for e in container))

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

def toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((index for (value, index) in patch))
    return patch

def uppermost(patch):
    return min((i for (i, j) in toindices(patch)))

def lowermost(patch):
    return max((i for (i, j) in toindices(patch)))

def leftmost(patch):
    return min((j for (i, j) in toindices(patch)))

def rightmost(patch):
    return max((j for (i, j) in toindices(patch)))

def rot90(grid):
    return tuple((row for row in zip(*grid[::-1])))

def hupscale(grid, factor):
    g = tuple()
    for row in grid:
        r = tuple()
        for value in row:
            r = r + tuple((value for num in range(factor)))
        g = g + (r,)
    return g

def vupscale(grid, factor):
    g = tuple()
    for row in grid:
        g = g + tuple((row for num in range(factor)))
    return g

def index(grid, loc):
    (i, j) = loc
    (h, w) = (len(grid), len(grid[0]))
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]]

def p(g):
    return [list(v) for v in solve_e26a3af2(tuple((tuple(r) for r in g)))]

def solve_e26a3af2(I):
    x1 = rot90(I)
    x2 = apply(mostcommon, I)
    x3 = apply(mostcommon, x1)
    x4 = repeat(x2, 1)
    x5 = repeat(x3, 1)
    x6 = compose(size, dedupe)
    x7 = x6(x2)
    x8 = x6(x3)
    x9 = greater(x8, x7)
    x10 = branch(x9, height, width)
    x11 = x10(I)
    x12 = rot90(x4)
    x13 = branch(x9, x5, x12)
    x14 = branch(x9, vupscale, hupscale)
    O = x14(x13, x11)
    return O