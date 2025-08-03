def p(g):
    h=[[w for w in v if w]for v in g]
    i=[v[::-1] for v in h if v]
    return i