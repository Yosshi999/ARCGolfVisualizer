def p(g):
    for i in range(len(g)):
        for j in range(len(g)):
            if g[i][j]:
                for x in[-1,1]:
                    for y in[-1,1]:
                        I=i
                        J=j
                        while 0<=I<len(g) and 0<=J<len(g):
                            g[I][J]=g[i][j]
                            I+=x
                            J+=y
                return g