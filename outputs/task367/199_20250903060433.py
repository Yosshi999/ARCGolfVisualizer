e=enumerate
def p(g,d=8):
 for y,v in e(g[1:]):
  for x,c in e(v[1:]):
   if sum(Q:=g[y][x:x+2]+v[x:x+2])==5==c:g[y+2][x+2]=4
   v[x+1]|=4*(4in Q)
 return p([*map(list,zip(*g))][::-1],d-1)if d else g