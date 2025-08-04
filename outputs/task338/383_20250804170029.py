def p(g):
    for i in range(len(g)):
        for j in range(len(g[0])):
            t=0
            f=0
            if 0<i and g[i-1][j]:t+=1;f+=1
            if i<len(g)-1 and g[i+1][j]:t+=1;f+=1
            if 0<j and g[i][j-1]:t+=1
            if j<len(g[0])-1 and g[i][j+1]:t+=1
            if g[i][j]<1:g[i][j]=9*(t>2 or (t==2 and f==1))
    return [[w//3for w in v]for v in g]