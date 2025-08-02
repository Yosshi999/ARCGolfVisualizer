def p(g):
 a=[0,0,0]
 for i in range(7):
  for j in range(7):
   if g[i][j]>0:a[(i+j)%3]=g[i][j]
 for i in range(7):
  for j in range(7):
   g[i][j]=a[(i+j)%3]
 return g