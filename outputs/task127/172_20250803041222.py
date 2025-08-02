def p(g):
 for i in range((len(g)+1)//4):
  for j in range((len(g[0])+1)//4):
   q=g[i*4+1][j*4+1]+5
   for u in range(3):
    for v in range(3):g[i*4+u][j*4+v]=q
 return g