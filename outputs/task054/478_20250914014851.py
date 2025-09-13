def p(g):
 B=g[0][0];f=sum(g,[]);C=max({*f}-{B},key=f.count)
 H=[(k//30,k%30)for k in range(870)if B!=f[k]!=C==f[k+1]]
 L=[k for k in range(900)if B!=f[k]!=C!=f[k+1]];I,J=divmod(L[len(L)//2],30)
 for i,j in H:
  for u in [-1,0,1]:
   for v in [-1,0,1]:
    if(a:=g[I+u][J+v])!=B:g[i+u][j+v]=a
  for u,v,x,y in[(i-2,j,-1,0),(i+2,j,1,0),(i,j-2,0,-1),(i,j+2,0,1)]:
   while g[u][v]!=B!=(a:=g[I+2*x][J+2*y]):g[u][v]=a;u+=x;v+=y
 for u in range(I-2,I+3):g[u][J-2:J+3]=[B]*5
 return g