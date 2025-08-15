def f(g):
 C=[[]for _ in range(10)]
 for v in g:
  for c in range(1,10):
   C[c]+=[sum(x==c for x in v)]
 T=0
 for c in range(1,10):
  S=set(C[c])-{0}
  if len(S)==1:F=c
  if len(S)==2and 1 not in S:T=c
 if T>0:
  s=max(C[T])-min(set(C[T])-{0})
  t=C[T].index(max(C[T]))
  u,v=g[t].index(F),g[t].index(T)
  if u>v:
   for i in range(len(g)):
    for j in range(u-1,-1,-1):
     if j-s>=0:g[i][j]=g[i][j-s]
     else:g[i][j]=0
  else:
   for i in range(len(g)):
    for j in range(v,len(g[0])):
     if j+s<len(g[0]):g[i][j]=g[i][j+s]
     else:g[i][j]=0
 return [*map(list,zip(*g))]
p=lambda g:f(f(g))