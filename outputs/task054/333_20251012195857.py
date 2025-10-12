def p(g):
 f=sum(g,[])
 B,*_=f;C=max({*f}-{B},key=f.count)
 H=[[],[]]
 for k in range(900):
  if B!=f[k]!=C:H[f[k+1]==C]+=k,
 L,H=H
 K=L[len(L)//2]
 for k in H:
  for u in L:
   if f[k+u-K]!=B:f[k+u-K]=f[u]
  for x in[-30,30,-1,1]:
   u=k+2*x;a=f[K+2*x]
   while f[u]!=B!=a:f[u]=a;u+=x
 for u in L:f[u]=B
 return[*zip(*[iter(f)]*30)]