def f(g):
 m=min(g,key=lambda x:(max(x)<1,-x.count(0)))
 c=max(m)
 if m.count(c)==1:
  i=g.index(m)
  if c in g[i-1]:g[1:i+1]=g[:i];return f(g)
 return[*zip(*g[::-1])]
p=lambda g:f(f(f(f(g))))