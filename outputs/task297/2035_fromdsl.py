ORIGIN = (0, 0)

def repeat(item, num):
    return tuple((item for i in range(num)))

def merge(containers):
    return type(containers)((e for c in containers for e in c))

def astuple(a, b):
    return (a, b)

def width(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece[0])
    return rightmost(piece) - leftmost(piece) + 1

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

def leftmost(patch):
    return min((j for (i, j) in toindices(patch)))

def rightmost(patch):
    return max((j for (i, j) in toindices(patch)))

def dmirror(piece):
    if isinstance(piece, tuple):
        return tuple(zip(*piece))
    (a, b) = ulcorner(piece)
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset(((v, (j - b + a, i - a + b)) for (v, (i, j)) in piece))
    return frozenset(((j - b + a, i - a + b) for (i, j) in piece))

def hupscale(grid, factor):
    g = tuple()
    for row in grid:
        r = tuple()
        for value in row:
            r = r + tuple((value for num in range(factor)))
        g = g + (r,)
    return g

def vconcat(a, b):
    return a + b

def index(grid, loc):
    (i, j) = loc
    (h, w) = (len(grid), len(grid[0]))
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]]

def tophalf(grid):
    return grid[:len(grid) // 2]

def p(g):
    return [list(v) for v in solve_bd4472b8(tuple((tuple(r) for r in g)))]

def solve_bd4472b8(I):
    x1 = width(I)
    x2 = astuple(2, x1)
    x3 = crop(I, ORIGIN, x2)
    x4 = tophalf(x3)
    x5 = dmirror(x4)
    x6 = hupscale(x5, x1)
    x7 = repeat(x6, 2)
    x8 = merge(x7)
    O = vconcat(x3, x8)
    return O