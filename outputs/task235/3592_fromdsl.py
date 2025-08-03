DOWN = (1, 0)
UNITY = (1, 1)

def add(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] + b[0], a[1] + b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a + b[0], a + b[1])
    return (a[0] + b, a[1] + b)

def multiply(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a * b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] * b[0], a[1] * b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a * b[0], a * b[1])
    return (a[0] * b, a[1] * b)

def double(n):
    return n * 2 if isinstance(n, int) else (n[0] * 2, n[1] * 2)

def size(container):
    return len(container)

def merge(containers):
    return type(containers)((e for c in containers for e in c))

def astuple(a, b):
    return (a, b)

def compose(outer, inner):
    return lambda x: outer(inner(x))

def chain(h, g, f):
    return lambda x: h(g(f(x)))

def matcher(function, target):
    return lambda x: function(x) == target

def rbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda x: function(x, fixed)
    elif n == 3:
        return lambda x, y: function(x, y, fixed)
    else:
        return lambda x, y, z: function(x, y, z, fixed)

def power(function, n):
    if n == 1:
        return function
    return compose(function, power(function, n - 1))

def fork(outer, a, b):
    return lambda x: outer(a(x), b(x))

def apply(function, container):
    return type(container)((function(e) for e in container))

def ofcolor(grid, value):
    return frozenset(((i, j) for (i, r) in enumerate(grid) for (j, v) in enumerate(r) if v == value))

def ulcorner(patch):
    return tuple(map(min, zip(*toindices(patch))))

def crop(grid, start, dims):
    return tuple((r[start[1]:start[1] + dims[1]] for r in grid[start[0]:start[0] + dims[0]]))

def toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((index for (value, index) in patch))
    return patch

def hupscale(grid, factor):
    g = tuple()
    for row in grid:
        r = tuple()
        for value in row:
            r = r + tuple((value for num in range(factor)))
        g = g + (r,)
    return g

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
    return [list(v) for v in solve_995c5fa3(tuple((tuple(r) for r in g)))]

def solve_995c5fa3(I):
    x1 = hsplit(I, 3)
    x2 = astuple(2, 1)
    x3 = rbind(ofcolor, 0)
    x4 = compose(ulcorner, x3)
    x5 = compose(size, x3)
    x6 = matcher(x5, 0)
    x7 = matcher(x4, UNITY)
    x8 = matcher(x4, DOWN)
    x9 = matcher(x4, x2)
    x10 = rbind(multiply, 3)
    x11 = power(double, 2)
    x12 = compose(double, x6)
    x13 = chain(x11, double, x7)
    x14 = compose(x10, x8)
    x15 = compose(x11, x9)
    x16 = fork(add, x12, x13)
    x17 = fork(add, x14, x15)
    x18 = fork(add, x16, x17)
    x19 = rbind(canvas, UNITY)
    x20 = compose(x19, x18)
    x21 = apply(x20, x1)
    x22 = merge(x21)
    O = hupscale(x22, 3)
    return O