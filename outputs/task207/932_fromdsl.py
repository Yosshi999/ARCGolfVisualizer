def combine(a, b):
    return type(a)((*a, *b))

def leastcommon(container):
    return min(set(container), key=container.count)

def astuple(a, b):
    return (a, b)

def rot90(grid):
    return tuple((row for row in zip(*grid[::-1])))

def rot270(grid):
    return tuple((tuple(row[::-1]) for row in zip(*grid[::-1])))[::-1]

def tophalf(grid):
    return grid[:len(grid) // 2]

def bottomhalf(grid):
    return grid[len(grid) // 2 + len(grid) % 2:]

def lefthalf(grid):
    return rot270(tophalf(rot90(grid)))

def righthalf(grid):
    return rot270(bottomhalf(rot90(grid)))

def p(g):
    return [list(v) for v in solve_88a62173(tuple((tuple(r) for r in g)))]

def solve_88a62173(I):
    x1 = lefthalf(I)
    x2 = righthalf(I)
    x3 = tophalf(x1)
    x4 = tophalf(x2)
    x5 = bottomhalf(x1)
    x6 = bottomhalf(x2)
    x7 = astuple(x3, x4)
    x8 = astuple(x5, x6)
    x9 = combine(x7, x8)
    O = leastcommon(x9)
    return O