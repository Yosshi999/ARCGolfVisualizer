def size(container):
    return len(container)

def first(container):
    return next(iter(container))

def remove(value, container):
    return type(container)((e for e in container if e != value))

def other(container, value):
    return first(remove(value, container))

def astuple(a, b):
    return (a, b)

def ofcolor(grid, value):
    return frozenset(((i, j) for (i, r) in enumerate(grid) for (j, v) in enumerate(r) if v == value))

def palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for (v, _) in element})

def canvas(value, dimensions):
    return tuple((tuple((value for j in range(dimensions[1]))) for i in range(dimensions[0])))

def p(g):
    return [list(v) for v in solve_d631b094(tuple((tuple(r) for r in g)))]

def solve_d631b094(I):
    x1 = palette(I)
    x2 = other(x1, 0)
    x3 = ofcolor(I, x2)
    x4 = size(x3)
    x5 = astuple(1, x4)
    O = canvas(x2, x5)
    return O