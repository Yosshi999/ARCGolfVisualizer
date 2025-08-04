def p(g):
 for j in range(10):
  if g[0][j]>0:
   for i in range(1,10):
    if g[i][j]>0:
     g[i][j]=g[0][j];break
  if g[9][j]>0:
   for i in range(8,0,-1):
    if g[i][j]>0:
     g[i][j]=g[9][j];break
  if g[j][0]>0:
   for i in range(1,10):
    if g[j][i]>0:
     g[j][i]=g[j][0];break
  if g[j][9]>0:
   for i in range(8,0,-1):
    if g[j][i]>0:
     g[j][i]=g[j][9];break
 return g