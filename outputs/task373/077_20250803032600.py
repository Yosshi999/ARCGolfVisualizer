def p(g):
 for j in range(1,6,2):
  g[0][j],g[1][j]=g[1][j],g[0][j]
 return g