def p(g):
 for k in range(81):
  if g[i:=k//9][j:=k%9]==1:
   g[i-1][j]=g[i+1][j]=7
   g[i][j-1:j+2]=[7,1,7]
  if g[i][j]==2:
   g[i-1][j-1:j+2]=g[i+1][j-1:j+2]=[4,0,4]
 return g