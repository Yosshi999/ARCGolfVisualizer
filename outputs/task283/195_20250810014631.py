def p(g):
 for i in range(10):
  for j in range(10):
   if g[i][j]==5:
    v=(i>0and g[i-1][j]>0)+(j>0and g[i][j-1]>0)+(i<9and g[i+1][j]>0)+(j<9and g[i][j+1]>0)-2
    g[i][j]=[1,4,2][v]
 return g