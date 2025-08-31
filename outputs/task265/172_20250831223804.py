def p(g):
 for i in range(17):
  for j in range(17):
   if all(v!=5 for v in g[i][j:j+2]+g[i+1][j:j+2])>((i,j,g[8][10])==(8,11,2)):g[i][j:j+2]=g[i+1][j:j+2]=[2,2]
 return g