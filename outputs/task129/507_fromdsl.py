THREE_BY_THREE = (3, 3)

def mostcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for (v, _) in element]
    return max(set(values), key=values.count)

def canvas(value, dimensions):
    return tuple((tuple((value for j in range(dimensions[1]))) for i in range(dimensions[0])))

def p(g):
    return [list(v) for v in solve_5582e5ca(tuple((tuple(r) for r in g)))]

def solve_5582e5ca(I):
    x1 = mostcolor(I)
    O = canvas(x1, THREE_BY_THREE)
    return O