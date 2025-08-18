e=enumerate
def p(g):
 r=[{(i,j)}for i,v in e(g)for j,x in e(v)if x==2]
 while r:
  w=r.pop();v,h=zip(*w)
  for t in r:
   if min(max(a-y,y-a,b-x,x-b)for a,b in w for y,x in t)<3:t|=w
  for i in range(min(v),max(v)+1):g[i]=[(x,4)[~5>>x&(min(h)<=j<=max(h))]for j,x in e(g[i])]
 return g