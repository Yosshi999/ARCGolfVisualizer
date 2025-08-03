ORIGIN = (0, 0)
UNITY = (1, 1)
DOWN_LEFT = (1, -1)

def combine(a, b):
    return type(a)((*a, *b))

def decrement(x):
    return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)

def tojvec(j):
    return (0, j)

def width(piece):
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece[0])
    return rightmost(piece) - leftmost(piece) + 1

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

def shoot(start, direction):
    return connect(start, (start[0] + 42 * direction[0], start[1] + 42 * direction[1]))

def p(g):
    return [list(v) for v in solve_ea786f4a(tuple((tuple(r) for r in g)))]

def solve_ea786f4a(I):
    x1 = width(I)
    x2 = shoot(ORIGIN, UNITY)
    x3 = decrement(x1)
    x4 = tojvec(x3)
    x5 = shoot(x4, DOWN_LEFT)
    x6 = combine(x2, x5)
    O = fill(I, 0, x6)
    return O