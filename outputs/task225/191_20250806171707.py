def p(g):
 for p in range(36):
  if g[i:=p//6][j:=p%6]:
   for q in range(16):
    k,l,x,y=map(int,f'{q:04b}')
    if 0<=(J:=j+2-4*y+l)<6*(0<=(I:=i+2-4*x+k)<6):g[I][J]=g[i+x][j+y]
   return g