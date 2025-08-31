e=enumerate
def p(g,d=3):
 G=[*map(list,zip(*g))][::-1]
 l=min(v:=[y for y,v in e(g)if any(v)]);r=max(v);m=1
 for y,v in e(G):
  if any(v*m)or len([c for c in v if c])>3:
   m=0
   for x,c in e(v[l:r+1]):G[y][x+l]=c or 2
 return p(G,d-1)if d else G