def f(g):
 for i in range(len(g)):
  for j in range(len(g[0])):
   if g[i][j]==3:return i*2+1,j*2+1
def p(g):
 H,W=f(g)
 for i in range(len(g)):
  for j in range(len(g[0])):
   if 0<=H-i<len(g):g[i][j]=g[i][j]or g[H-i][j]
   if 0<=W-j<len(g[0]):g[i][j]=g[i][j]or g[i][W-j]
 return g