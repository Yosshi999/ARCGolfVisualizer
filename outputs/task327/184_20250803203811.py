def p(g):
    h=[v+[0]*3for v in g]+[[0]*6for _ in g]
    for i in range(1,6):
        for j in range(1,6):
            if h[i-1][j-1]:
                h[i][j]=h[i-1][j-1]
    return h