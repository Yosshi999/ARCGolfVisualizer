def p(g):
 k=g[0].index(7)
 for j in range(len(g[0])):
  for i in range(g.index(min(g))-abs(j-k)):g[i][j]=7+(j-k)%2
 return g