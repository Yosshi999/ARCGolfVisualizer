def identity(x):
    return x

def order(container, compfunc):
    return tuple(sorted(container, key=compfunc))

def rbind(function, fixed):
    n = function.__code__.co_argcount
    if n == 2:
        return lambda x: function(x, fixed)
    elif n == 3:
        return lambda x, y: function(x, y, fixed)
    else:
        return lambda x, y, z: function(x, y, z, fixed)

def apply(function, container):
    return type(container)((function(e) for e in container))

def rot90(grid):
    return tuple((row for row in zip(*grid[::-1])))

def rot270(grid):
    return tuple((tuple(row[::-1]) for row in zip(*grid[::-1])))[::-1]

def p(g):
    return [list(v) for v in solve_1e0a9b12(tuple((tuple(r) for r in g)))]

def solve_1e0a9b12(I):
    x1 = rot270(I)
    x2 = rbind(order, identity)
    x3 = apply(x2, x1)
    O = rot90(x3)
    return O