def p(g):
    s=0
    I=0
    J=0
    K=0
    L=0
    for i in range(16):
        for j in range(16):
            for k in range(min(17-i,9)):
                for l in range(min(17-j,9)):
                    h=[v[j:j+l]for v in g[i:i+k]]
                    if g[i][j] and len(set(sum(h,[])))==1:
                        if s<k*l:
                            s=k*l
                            I=i
                            J=j
                            K=k
                            L=l
    return [[g[i][j]*(I<=i<I+K and J<=j<J+L)for j in range(16)]for i in range(16)]