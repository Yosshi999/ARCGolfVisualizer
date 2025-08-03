def p(g):
 for i in range(len(g[0])):
  if g[0][i]:
   g[1][i-1]=g[1][i+1]=g[0][i]
 return g[:2]*3