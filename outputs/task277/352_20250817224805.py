e=enumerate
def f(g):
 r=[]
 for i,v in e(g):
  for j,x in e(v):
   if x>0:
    c=[(i,j)];v[j]*=-1
    for p,q in c:
     for y in[p-1,p,p+1]:
      for x in[q-1,q,q+1]:
       if len(g)>y>-1<x<len(v)and g[y][x]>0:c+=[(y,x)];g[y][x]*=-1
    r+=[c]
 return sorted(r,key=len)
def p(g):
 for i,c in e(f(g)):
  for y,x in c:
   g[y][x]=max(2-i,1)
 return g