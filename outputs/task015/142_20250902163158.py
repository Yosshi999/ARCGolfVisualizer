def p(g,d=4):
 for k in range(81):
  c=g[i:=k//9][j:=k%9]
  if 0<c<3:g[i-1][j+c-1]=10-3*c
 return p([*map(list,zip(*g[::-1]))],d-1)if d else g