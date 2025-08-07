def p(g):
 for k in range(1000):
  i=k//10%10;j=k%10
  if i>0<j and(g[i][j]!=1)+g[i-1][j]+g[i][j-1]==0:g[i-1][j-1]=1
  if i<9>j and(g[i][j]!=2)+g[i+1][j]+g[i][j+1]==0:g[i+1][j+1]=2
 return g