def p(g):
 for c in[1,2]:
  for k in range(2000):
   i=k//10%10;j=k%10
   if i>0<j and(g[i][j]!=c)+g[i-1][j]+g[i][j-1]==0:g[i-1][j-1]=c
  g=[v[::-1]for v in g][::-1]
 return g