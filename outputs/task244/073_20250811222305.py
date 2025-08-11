def p(g):
 n=2
 while g[n-2]==g[n-1]:n+=1
 return[v[::-n]for v in g[::n]]