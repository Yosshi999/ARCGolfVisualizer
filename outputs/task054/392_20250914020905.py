def p(g):
 B=g[0][0];f=sum(g,[]);C=max({*f}-{B},key=f.count)
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
 for u in [-60,-30,0,30,60]:f[K+u-2:K+u+3]=[B]*5
 return[*zip(*[iter(f)]*30)]