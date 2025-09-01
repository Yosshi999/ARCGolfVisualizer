def p(g,d=4):
 v,*_,u,w=filter(max,g)
 if sum(v)==max(v):i=g.index(v);j=g.index(w);g[i:j+1]=[w]+[u]*(j-i)
 return p([*zip(*g[::-1])],d-1)if d else g