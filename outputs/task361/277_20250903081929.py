r=range(10)
e=enumerate
def p(g):
 _,q,p=max((d*(sum((v[x::d][:2]for v in g[y::d][:2]),[])==[g[y][x]]*4)*(g[y][x]>0),x-y,x+y+d)for d in r[1:]for x in r for y in r)
 for y,v in e(g):
  for x,c in e(v):
   Y=y
   for _ in'....':c|=g[Y%10][x%10];Y,x=p-x,Y+q
   g[Y][x]=c
 return g