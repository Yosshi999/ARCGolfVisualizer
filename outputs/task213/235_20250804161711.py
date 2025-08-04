def p(g):
    f=lambda x:len(set(x))
    v=max(g[0],g[-1],key=f)
    w=max([v[0]for v in g],[v[-1]for v in g],key=f)
    if f(v)<f(w):
        return [[c]*(f(w)-1)for c in w if c]
    else:
        return [[c for c in v if c]]*(f(v)-1)