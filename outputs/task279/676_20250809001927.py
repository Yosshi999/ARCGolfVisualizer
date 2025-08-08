def p(g):
 W=len(g[0]);H=len(g)
 for j in range(W):
  if g[0][j]==9:g[0][j]=0
  if g[-1][j]==9:g[-1][j]=0
 for i in range(H):
  if g[i][0]==9:g[i][0]=0
  if g[i][-1]==9:g[i][-1]=0
 for _ in range(900):
  for i in range(H):
   for j in range(W):
    if g[i][j]==9:
     if i>0 and g[i-1][j]<1 or i<H-1 and g[i+1][j]<1 or j>0 and g[i][j-1]<1 or j<W-1 and g[i][j+1]<1:g[i][j]=0
 for _ in range(900):
  for i in range(H):
   for j in range(W):
    if g[i][j]==1:
     if i>0 and g[i-1][j]in{8,9} or i<len(g)-1 and g[i+1][j]in{8,9} or j>0 and g[i][j-1]in{8,9} or j<len(g[0])-1 and g[i][j+1]in{8,9}:g[i][j]=8
 for i in range(H):
  for j in range(W):
   g[i][j]=g[i][j]or 9
 return g