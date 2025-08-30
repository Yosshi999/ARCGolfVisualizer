r=range
def p(g):
 def D(y,x):
  if 10>x>-1<y<10>0<g[y][x]:g[y][x]=0;return sum((D(y+a%3-1,x+a//3-1)for a in r(9)),[(y,x)])
  return[]
 for z in r(100):
  for q,p in(s:=D(z//10,z%10)):
   g[q][p]=1+(len(s)==6)
 return g