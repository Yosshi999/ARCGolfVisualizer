def first(container):
    return next(iter(container))

def last(container):
    return max(enumerate(container))[1]

def palette(element):
    if isinstance(element, tuple):
        return frozenset({v for r in element for v in r})
    return frozenset({v for (v, _) in element})

def replace(grid, replacee, replacer):
    return tuple((tuple((replacer if v == replacee else v for v in r)) for r in grid))

def switch(grid, a, b):
    return tuple((tuple((v if v != a and v != b else {a: b, b: a}[v] for v in r)) for r in grid))

def p(g):
    return [list(v) for v in solve_f76d97a5(tuple((tuple(r) for r in g)))]

def solve_f76d97a5(I):
    x1 = palette(I)
    x2 = first(x1)
    x3 = last(x1)
    x4 = switch(I, x2, x3)
    O = replace(x4, 5, 0)
    return O