E=enumerate
def p(g):
 a,b,c,d={*sum(g,[])}
 for _ in'.'*99:
  for i,v in E(g):
   for j,w in E(v):
    for y,x in(i+1,j),(i,j+1),(i-1,j),(i,j-1):
     if len(g)>y>-1<x<len(v)>1>w<(z:=g[y][x])%8:v[j]=z^a^b^c^d^8
 return g