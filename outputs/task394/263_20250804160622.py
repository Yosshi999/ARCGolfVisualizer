def p(g):
    n=len(g)
    c=[0]*n*n
    m=2+(n==7)
    for i in range(n):
        for j in range(n):
            if g[i][j]:
                c[i%m*m+j%m]=g[i][j]
    return [[c[i%m*m+j%m]for j in range(n) if g[i][j]<1]for i in range(n) if any(v==0for v in g[i])]