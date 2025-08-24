def f(g):
 m=min(g,key=lambda x:(max(x)<1,-x.count(0)))
 c=max(m)
 if m.count(c)==1:
  i=g.index(m)
  if c in g[i-1]:
   g=g[:1]+g[:i]+g[i+1:]
  else:
   g=g[:i]+g[i+1:]+g[:1]
  return f(g)
 return[*zip(*g)]
p=lambda g:f(f(g))