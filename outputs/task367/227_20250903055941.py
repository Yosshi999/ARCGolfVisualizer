r=range
def p(g,d=8):
 for y in r(len(g)-1):
  for x in r(len(g[0])-1):
   Q=g[y][x:x+2]+g[y+1][x:x+2]
   if g[y+1][x+1]==5==sum(Q):g[y+2][x+2]=4
   if 4 in Q:g[y+1][x+1]|=4
 return p([*map(list,zip(*g))][::-1],d-1) if d else g