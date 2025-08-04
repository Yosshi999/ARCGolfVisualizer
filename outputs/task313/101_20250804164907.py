def p(g):
    n=len(g)
    s=2+n//12
    return [[g[i%2][(j+1)%s]for j in range(n)]for i in range(n)]