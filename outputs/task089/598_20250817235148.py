e=enumerate
def p(g):
 r=[]
 for i,v in e(g):
  for j,x in e(v):
   if x>0:
    r+=[c:=[(i,j,x)]];v[j]*=-1
    for p,q,_ in c:
     for y in p-1,p,p+1:
      for x in q-1,q,q+1:
       if 13>y>-1<x<13and(l:=g[y][x])>0:c+=[(y,x,l)];g[y][x]*=-1
 r=sorted(r,key=len)
 B=[]
 for c in r:
  for Y,X,l in c:
   if l==2:B+=[(Y,X,c)]
 if B:
  Y,X,c=B[-1]
  for y,x,_ in B[:-1]:
    for i,j,l in c:
     g[i-Y+y][-j+X+x]=l
 B=[]
 for c in r:
  for Y,X,l in c:
   if l==3:B+=[(Y,X,c)]
 if B:
  Y,X,c=B[-1]
  for y,x,_ in B[:-1]:
    for i,j,l in c:
     g[i-Y+y][j-X+x]=l
 return[[abs(X)for X in v]for v in g]