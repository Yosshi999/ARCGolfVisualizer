def p(g):
 h=[[0]*9for v in g]
 for i in range(9):
  for j in range(9):
   if g[i][j]:
    h[i-1][j-1:j+2]=h[i+1][j-1:j+2]=[5,1,5]
    h[i][j-1:j+2]=[1,0,1]
 return h