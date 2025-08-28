R=range(100)
def D(g,y,x):
 if 0<=y<10>x>=0<g[y][x]:g[y][x]=0;return sum([D(g,y+i//3-1,x+i%3-1)for i in R[:9]],[(y,x)])
 return[]
def p(g,i=3):
 for v in sorted([D(g,i//10,i%10)for i in R],key=len):
  for y,x in v:g[y][x]=i%5
  i+=2
 return g