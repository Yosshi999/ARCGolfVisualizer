e=enumerate
def p(g):
 r=[]
 for i,v in e(g):
  for j,x in e(v):
   if x:
    r+=[c:=[(i,j)]]
    for p,q in c:
     for y in p-1,p,p+1:
      for x in q-1,q,q+1:
       if 10>y>-1<x<10and g[y][x]:c+=[(y,x)];g[y][x]=0
 for i,c in e(sorted(r,key=len)):
  for y,x in c:g[y][x]=2+-i//2
 return g