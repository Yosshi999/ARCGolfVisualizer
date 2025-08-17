e=enumerate
def p(g):
 r=[]
 for i,v in e(g):
  for j,x in e(v):
   if x>0:
    r+=[c:=[(i,j,x)]];v[j]*=-1
    for p,q,_ in c:
     for z in range(9):
      if 13>(y:=p-1+z//3)>-1<(x:=q-1+z%3)<13and(l:=g[y][x])>0:c+=[(y,x,l)];g[y][x]*=-1
 r=sorted(r,key=len)
 for m in[2,3]:
  if B:=[(Y,X,c)for c in r for Y,X,l in c if l==m]:
   Y,X,c=B[-1]
   for y,x,_ in B:
     for i,j,l in c:g[i-Y+y][[X-j,j-X][m>2or(Y,X)==(y,x)]+x]=l
 return g