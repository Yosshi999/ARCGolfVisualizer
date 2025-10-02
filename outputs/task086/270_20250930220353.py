e=enumerate
def p(g):
 for i,v in e(g):
  for j,w in e(v):
   if w>0:
    d=v[j+3]>0;B=g[i+1][j+1];r=range(~d,2*d+4)
    for x in r:
     for y in r:g[i+x][j+y]=-w if 0<y<d+2>x>0else-B if 0<=y<d+3>x>=0else-w if 0<=x&y<d+3else g[i+x][j+y]
 return[[*map(abs,v)]for v in g]