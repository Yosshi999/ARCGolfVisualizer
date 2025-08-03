def p(g):
    c=g[0][0]
    return [[c]*(sum(c!=v for v in g[0])+1)]*(sum(c!=v[0]for v in g)+1)