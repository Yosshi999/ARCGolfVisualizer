R=range(4)
def p(g):
 for p in range(36):
  if g[i:=p//6][j:=p%6]:
   for z in R:
    for k in R:
     x=z//2;y=z%2
     if 0<=(J:=j+2-4*y+k%2)<6*(0<=(I:=i+2-4*x+k//2)<6):g[I][J]=g[i+x][j+y]
   return g