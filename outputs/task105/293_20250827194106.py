e=enumerate
def f(g):
 I,J=zip(*[(i,j)for i,v in e(g)for j,w in e(v)if w])
 m=min(I);M=max(I);n=min(J);N=max(J)
 for v in g[m],g[M]:
  for j in range(n,N+1):v[j]=v[j]or 2
 for v in g:
  if v[n+1:N].count(1)>1:
   for j in range(n,N):v[j]=v[j]or 2
 return[*map(list,zip(*g))]
p=lambda g:f(f(g))