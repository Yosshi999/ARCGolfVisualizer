def p(g):
 for _ in[0]*4:
  v,*_,u,w=filter(max,g:=[*zip(*g[::-1])]);f=g.index
  if{*v}=={0,8}:g[f(v):f(u)]=[w]+[u]*(f(w)-f(v))
 return g