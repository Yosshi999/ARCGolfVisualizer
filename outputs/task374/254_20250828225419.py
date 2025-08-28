R=range(10)
def D(g,y,x):
 if 0<=y<10>x>=0<g[y][x]:g[y][x]=0;return sum([D(g,y+i//3-1,x+i%3-1)for i in R[:9]],[(y,x)])
 return[]
def p(g):
 for i,v in enumerate(sorted([D(g,y,x)for y in R for x in R],key=len)[-4:]):
  for y,x in v:g[y][x]=2*i%5
 return g