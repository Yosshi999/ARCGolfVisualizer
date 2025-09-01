def p(g):
 for _ in[0]*4:
  v,*_,u,w=filter(max,g:=[*zip(*g[::-1])])
  if sum(v)==max(v):i=g.index(v);j=g.index(w);g[i:j+1]=[w]+[u]*(j-i)
 return g