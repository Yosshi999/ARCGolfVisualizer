def difference(a, b):
    return type(a)((e for e in a if e not in b))

def first(container):
    return next(iter(container))

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

def shape(piece):
    return (height(piece), width(piece))

def sizefilter(container, n):
    return frozenset((item for item in container if len(item) == n))

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

def palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for (v, _) in element})

def color(obj):
    return next(iter(obj))[0]

def subgrid(patch, grid):
    return crop(grid, ulcorner(patch), shape(patch))

def replace(grid, replacee, replacer):
    return tuple((tuple((replacer if v == replacee else v for v in r)) for r in grid))

def index(grid, loc):
    (i, j) = loc
    (h, w) = (len(grid), len(grid[0]))
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]]

def trim(grid):
    return tuple((r[1:-1] for r in grid[1:-1]))

def p(g):
    return [list(v) for v in solve_3de23699(tuple((tuple(r) for r in g)))]

def solve_3de23699(I):
    x1 = fgpartition(I)
    x2 = sizefilter(x1, 4)
    x3 = first(x2)
    x4 = difference(x1, x2)
    x5 = first(x4)
    x6 = color(x3)
    x7 = color(x5)
    x8 = subgrid(x3, I)
    x9 = trim(x8)
    O = replace(x9, x7, x6)
    return O