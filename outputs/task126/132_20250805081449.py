def p(g):
 for i in range(len(g)-1):
  for j in range(len(g[0])-2):
   if g[i][j+1]==g[i+1][j]==g[i+1][j+2]>0:g[-1][j+1]=4
 return g