R=range
def p(g):
 H,W=len(g),len(g[0])
 def D(y,x):
  if H>y>=0<=x<W>3==g[y][x]:g[y][x]+=9;return sum((D(y+a%3-1,x+a//3-1)for a in R(9)),[(y,x)])
  return[]
 for y in R(H):
  for x in R(W):
   m=D(y,x);s=[sum(b*((y+a%3-1,x+a//3-1)in m)for a,b in[(1,1),(7,1),(3,4),(5,4)])for y,x in m]
   for y,x in m:g[y][x]=6if s.count(5)>1else 2if 6in s or 9in s else 1
 return g