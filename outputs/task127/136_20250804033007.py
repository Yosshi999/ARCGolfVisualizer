def p(g):
 for i in range(1,len(g),4):
  for j in range(1,len(g[0]),4):
   c=g[i][j]+5
   for v in g[i-1:i+2]:v[j-1:j+2]=[c]*3
 return g