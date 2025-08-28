R=range
def p(g):
 H=len(g);W=len(g[0])
 def D(y,x):
  if H>y>-1<x<W>0<g[y][x]:g[y][x]=0;return sum([D(y+i//3-1,x+i%3-1)for i in R(9)],[(y,x)])
  return[]
 n=len([*filter(len,[D(i//W,i%W)for i in R(H*W)])]);return[[8*(y==x)for x in R(n)]for y in R(n)]