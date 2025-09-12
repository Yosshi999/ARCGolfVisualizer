def p(g):
 for p in range(36):
  if g[i:=p//6][j:=p%6]:
   for q in range(16):
    x=q//2%2;y=q%2
    if 0<=(J:=j+2-4*y+q//4%2)<6*(0<=(I:=i+2-4*x+q//8)<6):g[I][J]=g[i+x][j+y]
   return g