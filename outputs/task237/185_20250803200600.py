def p(g):
    for v in g:
        for j in range(len(v)):
            v[j]=max(v[:j+1])
    for i in range(1,len(g)):
        if g[i][-1]<1:
            g[i][-1]=g[i-1][-1]
    return g