def p(g):
    j=0
    f=1
    for i in range(len(g)-1,-1,-1):
        g[i][j]=1
        j+=f
        if j>=len(g[0]):
            j-=2
            f=-1
        if j<0:
            j+=2
            f=1
    return [[w if w else 8for w in v]for v in g]