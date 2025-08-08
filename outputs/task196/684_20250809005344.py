def p(g):
 W=len(g[0]);H=len(g)
 for j in range(W):
  if g[0][j]==0:g[0][j]=9
  if g[-1][j]==0:g[-1][j]=9
 for i in range(H):
  if g[i][0]==0:g[i][0]=9
  if g[i][-1]==0:g[i][-1]=9
 for _ in range(900):
  for i in range(H):
   for j in range(W):
    if g[i][j]==0:
     if i>0 and g[i-1][j]==9 or i<H-1 and g[i+1][j]==9 or j>0 and g[i][j-1]==9 or j<W-1 and g[i][j+1]==9:g[i][j]=9
 for _ in range(900):
  for i in range(H):
   for j in range(W):
    if g[i][j]==1:
     if i>0 and g[i-1][j]in{0,3} or i<len(g)-1 and g[i+1][j]in{0,3} or j>0 and g[i][j-1]in{0,3} or j<len(g[0])-1 and g[i][j+1]in{0,3}:g[i][j]=3
 for i in range(H):
  for j in range(W):
   if g[i][j]==9:g[i][j]=0
 return g