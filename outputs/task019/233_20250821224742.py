e=enumerate
def p(g):
 z=[[0]*(2*len(g[0])+2)]
 h=z+[[0]+v*2+[0]for v in g*2]+z
 for i,v in e(h):
  for j,w in e(v):
   for x in[-1,1]:
    for y in[-1,1]:
     if w%8and h[i+x][j+y]%8<1:h[i+x][j+y]=8
 return[v[1:-1]for v in h[1:-1]]