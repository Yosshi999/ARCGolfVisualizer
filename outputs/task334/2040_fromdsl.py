RIGHT = (0, 1)
UNITY = (1, 1)
TWO_BY_TWO = (2, 2)
THREE_BY_THREE = (3, 3)

def equality(a, b):
    return a == b

def combine(a, b):
    return type(a)((*a, *b))

def first(container):
    return next(iter(container))

def remove(value, container):
    return type(container)((e for e in container if e != value))

def other(container, value):
    return first(remove(value, container))

def branch(condition, a, b):
    return a if condition else b

def fork(outer, a, b):
    return lambda x: outer(a(x), b(x))

def toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((index for (value, index) in patch))
    return patch

def palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for (v, _) in element})

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

def vfrontier(location):
    return frozenset(((i, location[1]) for i in range(30)))

def hfrontier(location):
    return frozenset(((location[0], j) for j in range(30)))

def p(g):
    return [list(v) for v in solve_d4469b4b(tuple((tuple(r) for r in g)))]

def solve_d4469b4b(I):
    x1 = palette(I)
    x2 = other(x1, 0)
    x3 = equality(x2, 1)
    x4 = equality(x2, 2)
    x5 = branch(x3, UNITY, TWO_BY_TWO)
    x6 = branch(x4, RIGHT, x5)
    x7 = fork(combine, vfrontier, hfrontier)
    x8 = x7(x6)
    x9 = canvas(0, THREE_BY_THREE)
    O = fill(x9, 5, x8)
    return O