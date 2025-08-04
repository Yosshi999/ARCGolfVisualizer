r=range(5)
def p(g):
 for i in r:
  for j in r:
   if g[i][j]:
    g[i][j]=0
    g[i-1][j-1]=3*(i*j>0)
    if i*(j<4):g[i-1][j+1]=6
    if j*(i<2):g[i+1][j-1]=8
    if j<4*(i<2):g[i+1][j+1]=7
    return g