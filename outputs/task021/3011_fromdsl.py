def difference(a, b):
    return type(a)((e for e in a if e not in b))

def size(container):
    return len(container)

def increment(x):
    return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)

def sfilter(container, condition):
    return type(container)((e for e in container if condition(e)))

def astuple(a, b):
    return (a, b)

def apply(function, container):
    return type(container)((function(e) for e in container))

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

def ulcorner(patch):
    return tuple(map(min, zip(*toindices(patch))))

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

def vline(patch):
    return height(patch) == len(patch) and width(patch) == 1

def dmirror(piece):
    if isinstance(piece, tuple):
        return tuple(zip(*piece))
    (a, b) = ulcorner(piece)
    if isinstance(next(iter(piece))[1], tuple):
        return frozenset(((v, (j - b + a, i - a + b)) for (v, (i, j)) in piece))
    return frozenset(((j - b + a, i - a + b) for (i, j) in piece))

def index(grid, loc):
    (i, j) = loc
    (h, w) = (len(grid), len(grid[0]))
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]]

def canvas(value, dimensions):
    return tuple((tuple((value for j in range(dimensions[1]))) for i in range(dimensions[0])))

def frontiers(grid):
    (h, w) = (len(grid), len(grid[0]))
    row_indices = tuple((i for (i, r) in enumerate(grid) if len(set(r)) == 1))
    column_indices = tuple((j for (j, c) in enumerate(dmirror(grid)) if len(set(c)) == 1))
    hfrontiers = frozenset({frozenset({(grid[i][j], (i, j)) for j in range(w)}) for i in row_indices})
    vfrontiers = frozenset({frozenset({(grid[i][j], (i, j)) for i in range(h)}) for j in column_indices})
    return hfrontiers | vfrontiers

def p(g):
    return [list(v) for v in solve_1190e5a7(tuple((tuple(r) for r in g)))]

def solve_1190e5a7(I):
    x1 = mostcolor(I)
    x2 = frontiers(I)
    x3 = sfilter(x2, vline)
    x4 = difference(x2, x3)
    x5 = astuple(x4, x3)
    x6 = apply(size, x5)
    x7 = increment(x6)
    O = canvas(x1, x7)
    return O