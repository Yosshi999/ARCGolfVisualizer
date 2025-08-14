def p(g):
 h=len(g)
 for c in range(1,len(g[0])):g[-1][c]=4;g[~c][c]=2
 return g