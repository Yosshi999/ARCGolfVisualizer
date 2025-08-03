def p(g):
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j]and g[i-1][j]*g[i+1][j]*g[i][j-1]*g[i][j+1]:
                g[i][j]=16
    return[[w&15for w in v]for v in g]