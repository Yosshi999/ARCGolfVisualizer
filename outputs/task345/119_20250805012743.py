def p(g):
 for i in range(8,-1,-1):
  for j in range(10):
   if g[i+1][j]&2:k=j+g[i][j]%2;g[i+1][k]=g[i][k]=2
 return g