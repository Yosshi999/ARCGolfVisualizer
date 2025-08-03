def p(g):
    h=[[0]*10for _ in[0]*10]
    for i in range(10):
        for j in range(10):
            if g[i][j]==8:
                h[i][j]=max(w if w%8else 0 for v in g[:i]for w in v[:j])
                h[i][j+1]=max(w if w%8else 0 for v in g[:i]for w in v[j:])
                h[i+1][j]=max(w if w%8else 0 for v in g[i:]for w in v[:j])
                h[i+1][j+1]=max(w if w%8else 0 for v in g[i:]for w in v[j:])
                return h