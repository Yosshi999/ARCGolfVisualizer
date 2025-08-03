def intersection(a, b):
    return a & b

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

def ofcolor(grid, value):
    return frozenset(((i, j) for (i, r) in enumerate(grid) for (j, v) in enumerate(r) if v == value))

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

def rot270(grid):
    return tuple((tuple(row[::-1]) for row in zip(*grid[::-1])))[::-1]

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

def tophalf(grid):
    return grid[:len(grid) // 2]

def bottomhalf(grid):
    return grid[len(grid) // 2 + len(grid) % 2:]

def lefthalf(grid):
    return rot270(tophalf(rot90(grid)))

def righthalf(grid):
    return rot270(bottomhalf(rot90(grid)))

def p(g):
    return [list(v) for v in solve_f2829549(tuple((tuple(r) for r in g)))]

def solve_f2829549(I):
    x1 = lefthalf(I)
    x2 = righthalf(I)
    x3 = ofcolor(x1, 0)
    x4 = ofcolor(x2, 0)
    x5 = intersection(x3, x4)
    x6 = shape(x1)
    x7 = canvas(0, x6)
    O = fill(x7, 3, x5)
    return O