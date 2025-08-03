def hupscale(grid, factor):
    g = tuple()
    for row in grid:
        r = tuple()
        for value in row:
            r = r + tuple((value for num in range(factor)))
        g = g + (r,)
    return g

def vupscale(grid, factor):
    g = tuple()
    for row in grid:
        g = g + tuple((row for num in range(factor)))
    return g

def hconcat(a, b):
    return tuple((i + j for (i, j) in zip(a, b)))

def vconcat(a, b):
    return a + b

def cellwise(a, b, fallback):
    (h, w) = (len(a), len(a[0]))
    resulting_grid = tuple()
    for i in range(h):
        row = tuple()
        for j in range(w):
            a_value = a[i][j]
            value = a_value if a_value == b[i][j] else fallback
            row = row + (value,)
        resulting_grid = resulting_grid + (row,)
    return resulting_grid

def p(g):
    return [list(v) for v in solve_007bbfb7(tuple((tuple(r) for r in g)))]

def solve_007bbfb7(I):
    x1 = hupscale(I, 3)
    x2 = vupscale(x1, 3)
    x3 = hconcat(I, I)
    x4 = hconcat(x3, I)
    x5 = vconcat(x4, x4)
    x6 = vconcat(x5, x4)
    O = cellwise(x2, x6, 0)
    return O