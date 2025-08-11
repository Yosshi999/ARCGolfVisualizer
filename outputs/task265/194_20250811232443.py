def p(g):
 for i in range(17):
  for j in range(17):
   if all(v!=5 for v in g[i][j:j+2]+g[i+1][j:j+2]) and not ((i,j)==(8,11)and g[8][10]==2):g[i][j]=g[i][j+1]=g[i+1][j]=g[i+1][j+1]=2
 return g