def p(g):
    Q=[]
    n=len(g)
    for i in range(n):
        Q+=(0,i),(i,0),(-1,i),(i,-1)
    for i,j in Q:
        if not g[i][j]:
            g[i][j]=4
            Q+=(i,(j-1)%n),((i-1)%n,j),((i+1)%n,j),(i,(j+1)%n)
    return[[(e^6)-2 for e in v]for v in g]