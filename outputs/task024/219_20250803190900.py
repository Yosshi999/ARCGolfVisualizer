def p(g):
 g=[*map(list,zip(*g))]
 for v in g:
  if 2in v:
   for j,x in enumerate(v):
    if x==0:v[j]=2
 g=[*map(list,zip(*g))]
 for i in range(len(g)):
  c=set(g[i])-{0,2}
  if c:g[i]=[list(c)[0]]*len(g[0])
 return g