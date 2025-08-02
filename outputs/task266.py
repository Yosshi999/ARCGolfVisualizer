def p(g):
 for i in range(3):
  for j in range(5):
   if g[i][j]==2:
    g[i][j]=0
    if i>0:
     if j>0:g[i-1][j-1]=3
     if j<4:g[i-1][j+1]=6
    if i<2:
     if j>0:g[i+1][j-1]=8
     if j<4:g[i+1][j+1]=7
 return g