def p(g):
 for i in range(len(g)):
  for j in range(len(g[0])):
   if (g[i][j]<1)*(i>0)*(j>0)*g[i][j-1]*g[i-1][j-1]*g[i-1][j]:g[i][j]=9
 return[[w//3for w in v]for v in g]