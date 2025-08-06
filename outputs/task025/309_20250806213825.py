def f(g):
 J={}
 for i,u in enumerate(g):
  if sum(v>0for v in u)==len(g[0]):J[u[0]]=i
 g=[*map(list,zip(*g))]
 if not J:return g
 for v in g:
  for j,c in enumerate(v):
   if c in J:
    if j<J[c]:
     v[j]=0;v[J[c]-1]=c
    if j>J[c]:
     v[j]=0;v[J[c]+1]=c
   elif c>0:v[j]=0
 return g
p=lambda g:f(f(g))