def p(g):
 x=y=-1
 for i in range(30):
  for j in range(len(g[0])):
   if g[i][j]:
    if x<0:x=i;y=j
    else:n=(x+i)//2;m=(y+j)//2;g[n-1][m]=g[n+1][m]=g[n][m-1]=g[n][m+1]=g[n][m]=3;return g