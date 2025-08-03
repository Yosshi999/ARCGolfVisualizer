def p(g):
    for v in g:
        s=sum(v)//2
        if s:
            i=g.index(v)
            for j in range(i):
                g[j][:s+i-j]=[3]*(s+i-j)
            for j in range(s):
                g[i+s-j][:j]=[1]*j
            return g