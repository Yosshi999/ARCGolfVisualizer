def p(g):
    for i in range(6):
        for j in range(6):
            if g[i][j]:
                for x in[-2,2]:
                    for y in[-2,2]:
                        for k in[0,1]:
                            for l in[0,1]:
                                if 0<=i+x+k<6 and 0<=j+y+l<6:
                                    g[i+x+k][j+y+l]=g[i+(2-x)//4][j+(2-y)//4]
                return g