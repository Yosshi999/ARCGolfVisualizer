def p(g):
    for i in range(9):
        for j in range(9):
            if g[i][j]==5:
                for x in[-1,0,1]:
                    for y in[-1,0,1]:
                        if x or y:
                            g[i+x][j+y]=1
    return g