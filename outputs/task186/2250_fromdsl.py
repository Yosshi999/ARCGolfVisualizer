ORIGIN = (0, 0)
UNITY = (1, 1)
THREE_BY_THREE = (3, 3)

def equality(a, b):
    return a == b

def size(container):
    return len(container)

def decrement(x):
    return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)

def tojvec(j):
    return (0, j)

def insert(value, container):
    return container.union(frozenset({value}))

def branch(condition, a, b):
    return a if condition else b

def ofcolor(grid, value):
    return frozenset(((i, j) for (i, r) in enumerate(grid) for (j, v) in enumerate(r) if v == value))

def toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((index for (value, index) in patch))
    return patch

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

def connect(a, b):
    (ai, aj) = a
    (bi, bj) = b
    si = min(ai, bi)
    ei = max(ai, bi) + 1
    sj = min(aj, bj)
    ej = max(aj, bj) + 1
    if ai == bi:
        return frozenset(((ai, j) for j in range(sj, ej)))
    elif aj == bj:
        return frozenset(((i, aj) for i in range(si, ei)))
    elif bi - ai == bj - aj:
        return frozenset(((i, j) for (i, j) in zip(range(si, ei), range(sj, ej))))
    elif bi - ai == aj - bj:
        return frozenset(((i, j) for (i, j) in zip(range(si, ei), range(ej - 1, sj - 1, -1))))
    return frozenset()

def p(g):
    return [list(v) for v in solve_794b24be(tuple((tuple(r) for r in g)))]

def solve_794b24be(I):
    x1 = ofcolor(I, 1)
    x2 = size(x1)
    x3 = decrement(x2)
    x4 = canvas(0, THREE_BY_THREE)
    x5 = tojvec(x3)
    x6 = connect(ORIGIN, x5)
    x7 = equality(x2, 4)
    x8 = insert(UNITY, x6)
    x9 = branch(x7, x8, x6)
    O = fill(x4, 2, x9)
    return O