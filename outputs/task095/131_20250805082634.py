r=range(9)
def p(g):
 for i in r:
  for j in r:
   if g[i][j]>1:
    for x in[-1,0,1]:g[i+x][j-1:j+2]=[1]*3
    g[i][j]=5
 return g