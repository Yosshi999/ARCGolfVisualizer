def p(g):
 r=range(len(g))
 for i in r:
  for j in r:
   if (g[i][j]<1)*i*j*g[i][j-1]*g[i-1][j-1]*g[i-1][j]:g[i][j]=9
 return[[w//3for w in v]for v in g]