r=range(9);R=[-1,0,1]
def p(g):
 for i in r:
  for j in r:
   if g[i][j]>1:
    for x in R:
     for y in R:
      if x|y:g[i+x][j+y]=1
 return g