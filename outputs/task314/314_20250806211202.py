def p(g):
 h=[[*v]for v in g]
 for i in [0,1]:
  for j in [0,1]:
   h[i][j+3]+=g[i][j]-1&g[i][j+6]-1
   h[i+3][j+3]+=g[i+3][j]-1&g[i+3][j+6]-1
   h[i+6][j+3]+=g[i+6][j]-1&g[i+6][j+6]-1
   h[i+3][j]+=g[i][j]-1&g[i+6][j]-1
   h[i+3][j+3]+=g[i][j+3]-1&g[i+6][j+3]-1
   h[i+3][j+6]+=g[i][j+6]-1&g[i+6][j+6]-1
 return h