def p(g):
 a=[0]*3
 for i in range(3):
  for j in range(3):
   if a[j]==0:a[j]=g[i][j]
   g[i][j]=a[j]
 return g