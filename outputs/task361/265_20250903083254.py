r=range
e=enumerate
def p(g):
 _,q,p=max((d*(len(s:={*g[y][x::d][:2],*g[y+d][x::d][:2]})<2)*min(s),x-y,x+y+d)for d in r(1,9)for x in r(9-d)for y in r(9-d))
 for y,v in e(g):
  for x,c in e(v):
   Y=y;X=x
   for _ in r(4):g[y][x]|=g[Y%10][X%10];Y,X=p-X,Y+q
 return g