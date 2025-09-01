def f(g):
 v,*_,u,w=filter(max,g)
 if sum(v)==max(v):i=g.index(v);j=g.index(w);g[i:j+1]=[w]+[u]*(j-i)
 return[*zip(*g[::-1])]
p=lambda g:f(f(f(f(g))))