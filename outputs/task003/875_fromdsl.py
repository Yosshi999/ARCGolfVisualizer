TWO_BY_ZERO = (2, 0)
THREE_BY_THREE = (3, 3)

def equality(a, b):
    return a == b

def branch(condition, a, b):
    return a if condition else b

def crop(grid, start, dims):
    return tuple((r[start[1]:start[1] + dims[1]] for r in grid[start[0]:start[0] + dims[0]]))

def vconcat(a, b):
    return a + b

def replace(grid, replacee, replacer):
    return tuple((tuple((replacer if v == replacee else v for v in r)) for r in grid))

def tophalf(grid):
    return grid[:len(grid) // 2]

def bottomhalf(grid):
    return grid[len(grid) // 2 + len(grid) % 2:]

def p(g):
    return [list(v) for v in solve_017c7c7b(tuple((tuple(r) for r in g)))]

def solve_017c7c7b(I):
    x1 = tophalf(I)
    x2 = bottomhalf(I)
    x3 = equality(x1, x2)
    x4 = crop(I, TWO_BY_ZERO, THREE_BY_THREE)
    x5 = branch(x3, x2, x4)
    x6 = vconcat(I, x5)
    O = replace(x6, 1, 2)
    return O