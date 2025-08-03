def c(x):
    x.sort()
    return (x[-1][0]-x[0][0]+1)*(x[-1][1]-x[0][1]+1)
def p(g):
    d=[[]for _ in[0]*10]
    for i in range(10):
        for j in range(10):
            if g[i][j]:
                d[g[i][j]].append((i,j))
    m=max([v for v in d if v],key=c)
    return [[d.index(m)]*2]*2