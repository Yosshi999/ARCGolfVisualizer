e=enumerate
def f(g):
 r=[]
 for i,v in e(g):
  for j,x in e(v):
   if x>0:
    r+=[[(i,j)]]
    for p,q in r[-1]:
     for y in[p-1,p,p+1]:
      for x in[q-1,q,q+1]:
       if len(g)>y>-1<x<len(v)and g[y][x]>0:r[-1]+=[(y,x)];g[y][x]*=-1
 return sorted(r,key=len)
def p(g):
 for i,c in e(f(g)):
  for y,x in c:g[y][x]=[2,1,1][i]
 return g