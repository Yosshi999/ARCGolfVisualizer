r=range
def p(g,d=4):
 for y in r(len(g)-1):
  for x in r(len(g[0])-1):
   if g[y+1][x+1]==5==sum(g[y][x:x+2]+g[y+1][x:x+2]):g[y+2][x+2]=4
   if g[y][x+1]==4or g[y+1][x]==4:g[y+1][x+1]|=4
 return p([*map(list,zip(*g))][::-1],d-1) if d else g