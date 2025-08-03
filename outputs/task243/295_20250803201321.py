def p(g):
    for _ in[0]*900:
        for i in range(len(g)):
            for j in range(len(g[0])):
                if g[i][j]==0 and ((i and g[i-1][j]==1) or (i<len(g)-1 and g[i+1][j]==1) or (j and g[i][j-1]==1) or (j<len(g[0])-1 and g[i][j+1]==1)):
                    g[i][j]=1
    return g