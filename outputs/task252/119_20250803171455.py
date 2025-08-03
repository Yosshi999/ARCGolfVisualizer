def p(g):
    return [[(4 if min(i,j)%2 else g[i][j])if g[i][j]else 0 for j in range(len(g[0]))]for i in range(len(g))]