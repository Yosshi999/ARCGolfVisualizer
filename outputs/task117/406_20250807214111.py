def p(g):
 T=[[1,0,1],[0,1,0],[1,0,1]]
 for i in range(len(g)-2):
  for j in range(len(g[0])-2):
   if g[i][j]>0and all(T[I][J]==g[i+I][j+J]==0 or T[I][J]>0and g[i+I][j+J]==g[i][j] for I in range(3) for J in range(3)):
    H=2*i+2;W=2*j+2
 for _ in "p"*3:
  for i in range(len(g)):
   for j in range(len(g[0])):
     if 0<=H-i<len(g):g[i][j]|=g[H-i][j]
     if 0<=W-j<len(g[0]):g[i][j]|=g[i][W-j]
 return g