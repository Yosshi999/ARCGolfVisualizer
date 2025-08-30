r=range
def p(g):
 def D(y,x):
  if 10>x>-1<y<10>0<(c:=g[y][x])!=8:g[y][x]=0;return sum((D(y+a//3,x+a%3-1)for a in[-2,0,2,4]),[(y,x,c)])
  return[]
 s=max(D(z//10,z%10) for z in r(100))
 (q,p,_),*_=s
 for z in r(100):
  if g[Y:=z//10][X:=z%10]==8:
   for y,x,c in s:g[Y-q+y][X-p+x]=c
 return g