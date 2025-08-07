def p(g):
 for c in[1,2]:
  for k in range(999):
   i=k//9%9;j=k%9
   if(g[i+1][j+1]!=c)+g[i][j+1]+g[i+1][j]==0:g[i][j]=c
  g=[v[::-1]for v in g][::-1]
 return g