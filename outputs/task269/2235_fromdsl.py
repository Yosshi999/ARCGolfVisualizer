def subtract(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] - b[0], a[1] - b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a - b[0], a - b[1])
    return (a[0] - b, a[1] - b)

def colorcount(element, value):
    if isinstance(element, tuple):
        return sum((row.count(value) for row in element))
    return sum((v == value for (v, _) in element))

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

def index(grid, loc):
    (i, j) = loc
    (h, w) = (len(grid), len(grid[0]))
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]]

def p(g):
    return [list(v) for v in solve_ac0a08a4(tuple((tuple(r) for r in g)))]

def solve_ac0a08a4(I):
    x1 = colorcount(I, 0)
    x2 = subtract(9, x1)
    O = upscale(I, x2)
    return O