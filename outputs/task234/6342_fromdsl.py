def multiply(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a * b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] * b[0], a[1] * b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a * b[0], a * b[1])
    return (a[0] * b, a[1] * b)

def equality(a, b):
    return a == b

def greater(a, b):
    return a > b

def size(container):
    return len(container)

def sfilter(container, condition):
    return type(container)((e for e in container if condition(e)))

def extract(container, condition):
    return next((e for e in container if condition(e)))

def first(container):
    return next(iter(container))

def last(container):
    return max(enumerate(container))[1]

def remove(value, container):
    return type(container)((e for e in container if e != value))

def other(container, value):
    return first(remove(value, container))

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

def fork(outer, a, b):
    return lambda x: outer(a(x), b(x))

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

def colorcount(element, value):
    if isinstance(element, tuple):
        return sum((row.count(value) for row in element))
    return sum((v == value for (v, _) in element))

def ulcorner(patch):
    return tuple(map(min, zip(*toindices(patch))))

def lrcorner(patch):
    return tuple(map(max, zip(*toindices(patch))))

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

def ineighbors(loc):
    return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})

def fgpartition(grid):
    return frozenset((frozenset(((v, (i, j)) for (i, r) in enumerate(grid) for (j, v) in enumerate(r) if v == value)) for value in palette(grid) - {mostcolor(grid)}))

def uppermost(patch):
    return min((i for (i, j) in toindices(patch)))

def lowermost(patch):
    return max((i for (i, j) in toindices(patch)))

def leftmost(patch):
    return min((j for (i, j) in toindices(patch)))

def rightmost(patch):
    return max((j for (i, j) in toindices(patch)))

def vmatching(a, b):
    return len(set((j for (i, j) in toindices(a))) & set((j for (i, j) in toindices(b)))) > 0

def manhattan(a, b):
    return min((abs(ai - bi) + abs(aj - bj) for (ai, aj) in toindices(a) for (bi, bj) in toindices(b)))

def adjacent(a, b):
    return manhattan(a, b) == 1

def palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for (v, _) in element})

def color(obj):
    return next(iter(obj))[0]

def toobject(patch, grid):
    (h, w) = (len(grid), len(grid[0]))
    return frozenset(((grid[i][j], (i, j)) for (i, j) in toindices(patch) if 0 <= i < h and 0 <= j < w))

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

def cover(grid, patch):
    return fill(grid, mostcolor(grid), toindices(patch))

def backdrop(patch):
    if len(patch) == 0:
        return frozenset({})
    indices = toindices(patch)
    (si, sj) = ulcorner(indices)
    (ei, ej) = lrcorner(patch)
    return frozenset(((i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1)))

def gravitate(source, destination):
    (si, sj) = center(source)
    (di, dj) = center(destination)
    (i, j) = (0, 0)
    if vmatching(source, destination):
        i = 1 if si < di else -1
    else:
        j = 1 if sj < dj else -1
    (gi, gj) = (i, j)
    c = 0
    while not adjacent(source, destination) and c < 42:
        c += 1
        gi += i
        gj += j
        source = shift(source, (i, j))
    return (gi - i, gj - j)

def outbox(patch):
    (ai, aj) = (uppermost(patch) - 1, leftmost(patch) - 1)
    (bi, bj) = (lowermost(patch) + 1, rightmost(patch) + 1)
    (si, sj) = (min(ai, bi), min(aj, bj))
    (ei, ej) = (max(ai, bi), max(aj, bj))
    vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
    hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
    return frozenset(vlines | hlines)

def p(g):
    return [list(v) for v in solve_98cf29f8(tuple((tuple(r) for r in g)))]

def solve_98cf29f8(I):
    x1 = fgpartition(I)
    x2 = fork(multiply, height, width)
    x3 = fork(equality, size, x2)
    x4 = extract(x1, x3)
    x5 = other(x1, x4)
    x6 = color(x5)
    x7 = rbind(greater, 3)
    x8 = rbind(toobject, I)
    x9 = rbind(colorcount, x6)
    x10 = chain(x8, ineighbors, last)
    x11 = chain(x7, x9, x10)
    x12 = sfilter(x5, x11)
    x13 = outbox(x12)
    x14 = backdrop(x13)
    x15 = cover(I, x5)
    x16 = gravitate(x14, x4)
    x17 = shift(x14, x16)
    O = fill(x15, x6, x17)
    return O