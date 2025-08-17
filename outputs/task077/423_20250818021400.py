e=enumerate
def p(g):
 r=[]
 for i,v in e(g):
  for j,x in e(v):
   if x==2:
    for w in r:
     if min(abs(i-y)+abs(j-x)for y,x in w)<3:w+=[(i,j)];break
    else:r+=[[(i,j)]]
 while r:
  w=r.pop()
  for t in r:
   if min(max(abs(a-y),abs(b-x))for a,b in w for y,x in t)<3:t+=w;break
  else:
    v,h=zip(*w)
    for i in range(min(v),max(v)+1):
     g[i]=[(4,x)[(5>>x&1)|1-(min(h)<=j<=max(h))]for j,x in e(g[i])]
 return g