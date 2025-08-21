E=enumerate
def p(g):
 (u,l),*_,(d,r)=((i,j)for i,v in E(g)for j,x in E(v)if x&4);B={(i,j,x)for i,v in E(g)for j,x in E(v)if(u<=i<=d)*(l<=j<=r)==0<x};v,h,_=zip(*B);B={(i-min(v),j-min(h)):x for(i,j,x)in B};H=range(u,d+1);W=range(l,r+1)
 for e in 2,3,4:
  for i in H:
   for j in W:
    if all(g[y][x]in[0,B.get(((y-i)//e,(x-j)//e),4)]for y in H for x in W):return[[B.get(((y-i)//e,(x-j)//e),g[y][x])for x in W]for y in H]