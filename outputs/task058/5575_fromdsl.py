DOWN = (1, 0)
UNITY = (1, 1)

def subtract(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] - b[0], a[1] - b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a - b[0], a - b[1])
    return (a[0] - b, a[1] - b)

def even(n):
    return n % 2 == 0

def initset(value):
    return frozenset({value})

def decrement(x):
    return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)

def insert(value, container):
    return container.union(frozenset({value}))

def astuple(a, b):
    return (a, b)

def branch(condition, a, b):
    return a if condition else b

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

def power(function, n):
    if n == 1:
        return function
    return compose(function, power(function, n - 1))

def fork(outer, a, b):
    return lambda x: outer(a(x), b(x))

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

def ulcorner(patch):
    return tuple(map(min, zip(*toindices(patch))))

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

def fill(grid, value, patch):
    (h, w) = (len(grid), len(grid[0]))
    grid_filled = list((list(row) for row in grid))
    for (i, j) in toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_filled[i][j] = value
    return tuple((tuple(row) for row in grid_filled))

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

def upscale(element, factor):
    if isinstance(element, tuple):
        g = tuple()
        for row in element:
            upscaled_row = tuple()
            for value in row:
                upscaled_row = upscaled_row + tuple((value for num in range(factor)))
            g = g + tuple((upscaled_row for num in range(factor)))
        return g
    else:
        if len(element) == 0:
            return frozenset()
        (di_inv, dj_inv) = ulcorner(element)
        (di, dj) = (-di_inv, -dj_inv)
        normed_obj = shift(element, (di, dj))
        o = set()
        for (value, (i, j)) in normed_obj:
            for io in range(factor):
                for jo in range(factor):
                    o.add((value, (i * factor + io, j * factor + jo)))
        return shift(frozenset(o), (di_inv, dj_inv))

def hconcat(a, b):
    return tuple((i + j for (i, j) in zip(a, b)))

def vconcat(a, b):
    return a + b

def index(grid, loc):
    (i, j) = loc
    (h, w) = (len(grid), len(grid[0]))
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]]

def canvas(value, dimensions):
    return tuple((tuple((value for j in range(dimensions[1]))) for i in range(dimensions[0])))

def p(g):
    return [list(v) for v in solve_28e73c20(tuple((tuple(r) for r in g)))]

def solve_28e73c20(I):
    x1 = width(I)
    x2 = astuple(1, 2)
    x3 = astuple(2, 2)
    x4 = astuple(2, 1)
    x5 = astuple(3, 1)
    x6 = canvas(3, UNITY)
    x7 = upscale(x6, 4)
    x8 = initset(DOWN)
    x9 = insert(UNITY, x8)
    x10 = insert(x2, x9)
    x11 = insert(x3, x10)
    x12 = fill(x7, 0, x11)
    x13 = vupscale(x6, 5)
    x14 = hupscale(x13, 3)
    x15 = insert(x4, x9)
    x16 = insert(x5, x15)
    x17 = fill(x14, 0, x16)
    x18 = even(x1)
    x19 = branch(x18, x12, x17)
    x20 = canvas(0, UNITY)
    x21 = lbind(hupscale, x20)
    x22 = chain(x21, decrement, height)
    x23 = rbind(hconcat, x6)
    x24 = compose(x23, x22)
    x25 = lbind(hupscale, x6)
    x26 = compose(x25, height)
    x27 = fork(vconcat, x24, rot90)
    x28 = fork(vconcat, x26, x27)
    x29 = subtract(x1, 4)
    x30 = power(x28, x29)
    O = x30(x19)
    return O