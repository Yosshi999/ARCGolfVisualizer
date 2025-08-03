def subtract(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] - b[0], a[1] - b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a - b[0], a - b[1])
    return (a[0] - b, a[1] - b)

def decrement(x):
    return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)

def first(container):
    return next(iter(container))

def last(container):
    return max(enumerate(container))[1]

def astuple(a, b):
    return (a, b)

def height(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece)
    return lowermost(piece) - uppermost(piece) + 1

def ofcolor(grid, value):
    return frozenset(((i, j) for (i, r) in enumerate(grid) for (j, v) in enumerate(r) if v == value))

def ulcorner(patch):
    return tuple(map(min, zip(*toindices(patch))))

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

def uppermost(patch):
    return min((i for (i, j) in toindices(patch)))

def lowermost(patch):
    return max((i for (i, j) in toindices(patch)))

def vmirror(piece):
    if isinstance(piece, tuple):
        return tuple((row[::-1] for row in piece))
    d = ulcorner(piece)[1] + lrcorner(piece)[1]
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset(((v, (i, d - j)) for (v, (i, j)) in piece))
    return frozenset(((i, d - j) for (i, j) in piece))

def hconcat(a, b):
    return tuple((i + j for (i, j) in zip(a, b)))

def vconcat(a, b):
    return a + b

def hsplit(grid, n):
    (h, w) = (len(grid), len(grid[0]) // n)
    offset = len(grid[0]) % n != 0
    return tuple((crop(grid, (0, w * i + i * offset), (h, w)) for i in range(n)))

def index(grid, loc):
    (i, j) = loc
    (h, w) = (len(grid), len(grid[0]))
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]]

def canvas(value, dimensions):
    return tuple((tuple((value for j in range(dimensions[1]))) for i in range(dimensions[0])))

def p(g):
    return [list(v) for v in solve_b0c4d837(tuple((tuple(r) for r in g)))]

def solve_b0c4d837(I):
    x1 = ofcolor(I, 5)
    x2 = ofcolor(I, 8)
    x3 = height(x1)
    x4 = decrement(x3)
    x5 = height(x2)
    x6 = subtract(x4, x5)
    x7 = astuple(1, x6)
    x8 = canvas(8, x7)
    x9 = subtract(6, x6)
    x10 = astuple(1, x9)
    x11 = canvas(0, x10)
    x12 = hconcat(x8, x11)
    x13 = hsplit(x12, 2)
    x14 = first(x13)
    x15 = last(x13)
    x16 = vmirror(x15)
    x17 = vconcat(x14, x16)
    x18 = astuple(1, 3)
    x19 = canvas(0, x18)
    O = vconcat(x17, x19)
    return O