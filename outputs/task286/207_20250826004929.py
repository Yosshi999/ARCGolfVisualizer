E=enumerate
def p(g):
 for _ in'.'*41:
  for i,v in E(g):
   for j,w in E(v):
    for y,x in(i+1,j),(i,j+1),(i-1,j),(i,j-1):
     if len(g)>y>-1<x<len(v)>w<(z:=g[y][x])%8:v[j]=sum({*sum(g,[])})-z-8
 return g