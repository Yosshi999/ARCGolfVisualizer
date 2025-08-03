def combine(a, b):
    return type(a)((*a, *b))

def order(container, compfunc):
    return tuple(sorted(container, key=compfunc))

def repeat(item, num):
    return tuple((item for i in range(num)))

def size(container):
    return len(container)

def merge(containers):
    return type(containers)((e for c in containers for e in c))

def last(container):
    return max(enumerate(container))[1]

def remove(value, container):
    return type(container)((e for e in container if e != value))

def apply(function, container):
    return type(container)((function(e) for e in container))

def papply(function, a, b):
    return tuple((function(i, j) for (i, j) in zip(a, b)))

def mpapply(function, a, b):
    return merge(papply(function, a, b))

def toindices(patch):
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((index for (value, index) in patch))
    return patch

def recolor(value, patch):
    return frozenset(((value, index) for index in toindices(patch)))

def partition(grid):
    return frozenset((frozenset(((v, (i, j)) for (i, r) in enumerate(grid) for (j, v) in enumerate(r) if v == value)) for value in palette(grid)))

def palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for (v, _) in element})

def color(obj):
    return next(iter(obj))[0]

def paint(grid, obj):
    (h, w) = (len(grid), len(grid[0]))
    grid_painted = list((list(row) for row in grid))
    for (value, (i, j)) in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_painted[i][j] = value
    return tuple((tuple(row) for row in grid_painted))

def index(grid, loc):
    (i, j) = loc
    (h, w) = (len(grid), len(grid[0]))
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]]

def p(g):
    return [list(v) for v in solve_bda2d7a6(tuple((tuple(r) for r in g)))]

def solve_bda2d7a6(I):
    x1 = partition(I)
    x2 = order(x1, size)
    x3 = apply(color, x2)
    x4 = last(x2)
    x5 = remove(x4, x2)
    x6 = repeat(x4, 1)
    x7 = combine(x6, x5)
    x8 = mpapply(recolor, x3, x7)
    O = paint(I, x8)
    return O