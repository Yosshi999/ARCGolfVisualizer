r=range
def p(g):
 H=len(g);W=len(g[0])
 def D(y,x):
  if H>y>-1<x<W>0<(c:=g[y][x]):g[y][x]=0;return sum((D(y+a%3-1,x+a//3-1)for a in r(9)),[c])
  return[]
 return[[8*any([1 for y in r(H)for x in r(W)if D(y,x).count(2)>4])]]