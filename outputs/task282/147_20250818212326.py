def p(g):
 h=[[0]*9for v in g]
 for k in range(81):
  if g[i:=k//9][j:=k%9]:h[i-1][j-1:j+2]=h[i+1][j-1:j+2]=[5,1,5];h[i][j-1:j+2]=[1,0,1]
 return h