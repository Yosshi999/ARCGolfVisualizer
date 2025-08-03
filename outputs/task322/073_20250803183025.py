def p(g):
 for i in[1,2]:g[i]=[a+b for a,b in zip(g[i-1],g[i])]
 return g