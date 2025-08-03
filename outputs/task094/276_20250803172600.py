def p(g):
    for i in range(2,13):
        for j in range(2,13):
            if g[i-2][j]*g[i+2][j]*g[i][j-2]*g[i][j+2]<2:
                g[i][j]=6
    return [[6if g[i][j]==8 and (g[i].count(6) or sum(g,[])[j::15].count(6))else g[i][j]for j in range(15)]for i in range(15)]