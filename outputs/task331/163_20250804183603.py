r=range(10)
def p(g):
 for i in r:
  for j in r:
   if g[i][j]%2:
    if i:g[i-1][j]=2
    if i<9:g[i+1][j]=8
    if j:g[i][j-1]=7
    if j<9:g[i][j+1]=6
 return g