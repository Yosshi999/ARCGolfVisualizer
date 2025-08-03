def p(g):
    for v in g[1:]:
        for j in range(len(v)-2):
            if v[j]*v[j+2] and v[j+1]<1 and g[g.index(v)-1][j+1]:
                g[-1][j+1]=4
    return g