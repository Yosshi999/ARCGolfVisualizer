e=enumerate
def p(g,d=4):
 for y,v in e(g[:-1]):
  for x,c in e(v):
   if[2,2]in[g[y+1][x-2+k:x+k]for k in range(4)]+[g[y][x+1:x+3],g[y][x-2:x]]:g[y][x]=3
 return p([*map(list,zip(*g))][::-1],d-1)if d else g