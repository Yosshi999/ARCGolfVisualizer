def p(g):
    c=len(set(sum(g,[])))
    if c==1:
        return [[5]*3]+[[0]*3]*2
    elif c==2:
        return [[5,0,0],[0,5,0],[0,0,5]]
    else:
        return [[0,0,5],[0,5,0],[5,0,0]]