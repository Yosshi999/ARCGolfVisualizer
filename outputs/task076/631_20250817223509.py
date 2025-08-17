e=enumerate
def f(g):
 r=[]
 for i,v in e(g):
  for j,x in e(v):
   if x>0:
    c=[(i,j,x)];v[j]*=-1
    for p,q,_ in c:
     for y in[p-1,p,p+1]:
      for x in[q-1,q,q+1]:
       if len(g)>y>-1<x<len(v)and(l:=g[y][x])>0:c+=[(y,x,l)];g[y][x]*=-1
    r+=[c]
 return max(r,key=len)
def p(g):
 H,W,P=len(g),len(g[0]),f(g)
 for i in range(-H,H*2):
  for j in range(-W,W*2):
   for b in range(8):
    X=[(*(lambda y,x:[i+[y,-y][b%2],j+[x,-x][b//2%2]][::[1,-1][b//4]])(*p),l)for*p,l in P]
    if all(len(g)>a>-1<b<len(g[0])and(l in[1,3]or g[a][b]+l==0)for a,b,l in X):
     for a,b,l in X:g[a][b]=l
 return[[abs(x)for x in v]for v in g]