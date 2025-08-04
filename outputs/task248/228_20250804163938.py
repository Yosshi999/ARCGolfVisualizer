def p(g):
    j=0
    c=g[-1][j]
    f=1
    for i in range(len(g)-1,-1,-1):
        g[i][j]=c
        j+=f
        if j>=len(g[0]):
            j-=2
            f=-1
        if j<0:
            j+=2
            f=1
    return g