def p(g):
    n=len(g)//2
    h=[v[:n]+v[:n][::-1]for v in g[:n]]
    h=[[g[0][n]if w else 0 for w in v]for v in h]
    return h+h[::-1]