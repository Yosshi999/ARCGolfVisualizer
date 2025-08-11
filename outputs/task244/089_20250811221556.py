def p(g):
 n=min(i for i in range(len(g))if g[0]!=g[i])+1
 return[v[::-n]for v in g[::n]]