def p(g):
 r=range(len(g)-1)
 for i in r:
  for j in r:
   if g[i][j]*g[i][j+1]*g[i+1][j]:g[i-1][j-1:j+2]=g[i+1][j-1:j+2]=[4]*3;g[i][j-1]=g[i][j+1]=4;return g