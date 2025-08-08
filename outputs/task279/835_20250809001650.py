def p(g):
 for j in range(len(g[0])):
  if g[0][j]==9:g[0][j]=0
  if g[-1][j]==9:g[-1][j]=0
 for i in range(len(g)):
  if g[i][0]==9:g[i][0]=0
  if g[i][-1]==9:g[i][-1]=0
 for _ in range(900):
  for i in range(len(g)):
   for j in range(len(g[0])):
    if g[i][j]==9:
     if i>0 and g[i-1][j]==0 or i<len(g)-1 and g[i+1][j]==0 or j>0 and g[i][j-1]==0 or j<len(g[0])-1 and g[i][j+1]==0:g[i][j]=0
 for _ in range(900):
  for i in range(len(g)):
   for j in range(len(g[0])):
    if g[i][j]==1:
     if i>0 and g[i-1][j]==9 or i<len(g)-1 and g[i+1][j]==9 or j>0 and g[i][j-1]==9 or j<len(g[0])-1 and g[i][j+1]==9:g[i][j]=8
     if i>0 and g[i-1][j]==8 or i<len(g)-1 and g[i+1][j]==8 or j>0 and g[i][j-1]==8 or j<len(g[0])-1 and g[i][j+1]==8:g[i][j]=8
 for i in range(len(g)):
  for j in range(len(g[0])):
   g[i][j]=g[i][j]or 9
 return g