r=range(10);R=range(4)
def p(g):
 f=0
 for I in r:
  for J in r:
   if g[I][J]%5:f=1;break
  if f:break
 for i in r:
  for j in r:
   if g[i][j]==5:
    for x in R:
     for y in R:
      if i+x<10*(j+y<10*(I+x<10*(J+y<10))):g[i+x][j+y]=g[I+x][J+y]
 return g