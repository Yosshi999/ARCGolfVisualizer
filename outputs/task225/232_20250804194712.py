r=range(6);R=[0,1]
def p(g):
 for i in r:
  for j in r:
   if g[i][j]:
    for x in R:
     for y in R:
      for k in R:
       for l in R:
        I=i+2-4*x+k;J=j+2-4*y+l
        if 0<=J<6*(0<=I<6):g[I][J]=g[i+x][j+y]
    return g