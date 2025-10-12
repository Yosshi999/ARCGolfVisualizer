def p(g):
 f=sum(g,[])
 B,*_=f;C=max({*f}-{B},key=f.count)
 H=[[],[]]
 for k in range(900):
  if B!=f[k]!=C:H[f[k+1]==C]+=k,
 L,H=H
 K=L[len(L)//2]
 for k in H:
  for u in [-31,-30,-29,-1,0,1,29,30,31]:
   if(a:=f[K+u])!=B:f[k+u]=a
  for x in [-30,30,-1,1]:
   u=k+2*x
   while f[u]!=B!=(a:=f[K+2*x]):f[u]=a;u+=x
 for u in L:f[u]=B
 return[*zip(*[iter(f)]*30)]