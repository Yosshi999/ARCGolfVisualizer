def leastcolor(element):
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for (v, _) in element]
    return min(set(values), key=values.count)

def replace(grid, replacee, replacer):
    return tuple((tuple((replacer if v == replacee else v for v in r)) for r in grid))

def p(g):
    return [list(v) for v in solve_aabf363d(tuple((tuple(r) for r in g)))]

def solve_aabf363d(I):
    x1 = leastcolor(I)
    x2 = replace(I, x1, 0)
    x3 = leastcolor(x2)
    O = replace(x2, x3, x1)
    return O