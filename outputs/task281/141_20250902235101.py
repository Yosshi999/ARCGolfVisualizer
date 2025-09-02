def p(g):
 for _ in[0]*4:
  v,*_,u,w=filter(max,g:=[*zip(*g[::-1])]);f=g.index
  if{*v}=={0,8}:i=f(v);j=f(w);g[i:j+1]=[w]+[u]*(j-i)
 return g