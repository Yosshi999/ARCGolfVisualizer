r=range(6);R=[0,1]
def p(g):
 for i in r:
  for j in r:
   if g[i][j]:
    for x in R:
     for y in R:
      for k in range(4):
       if 0<=(J:=j+2-4*y+k%2)<6*(0<=(I:=i+2-4*x+k//2)<6):g[I][J]=g[i+x][j+y]
    return g