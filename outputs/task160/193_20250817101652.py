def p(g):
 for i in range(8):
  for j in range(8):
   if g[i][j:j+3]==g[i+2][j:j+3]==[1,1,1]and g[i+1][j:j+3]==[1,0,1]:
    g[i][j:j+3]=g[i+2][j:j+3]=[0,2,0]
    g[i+1][j:j+3]=[2,2,2]
 return g