R=range(10)
def p(g):
 def D(y,x):
  if y<10>x>=0<g[y][x]:g[y][x]=0;return[(y,x)]+D(y+1,x)+D(y,x+1)
  return[]
 v=sorted([D(y,x)for y in R for x in R],key=len)[98:]
 for i in 0,1:
  (u,l),*_,(d,r)=sorted(v[i])
  for y in range(u,d+1):
   for x in range(l,r+1):g[y][x]=(u<y<d)*(l<x<r)*(i+1)or 4
 return g