def p(g):
 h=[list(v)for v in g]
 for i in range(8):
  for j in range(8):
   if g[i+2][j+2]>0and g[i+2][j+1]==g[i+2][j+3]==g[i+1][j+2]==g[i+3][j+2]:
    h[i][j]=h[i+1][j+1]=h[i+3][j+3]=h[i+4][j+4]=h[i][j+4]=h[i+1][j+3]=h[i+3][j+1]=h[i+4][j]=g[i+2][j+2]
    h[i][j+2]=h[i+2][j]=h[i+2][j+4]=h[i+4][j+2]=g[i+2][j+1]
 return h