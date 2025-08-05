def f(g):
 g=[*map(list,zip(*g))][::-1]
 a=max(i for i,v in enumerate(g)if 2in v)+1
 b=min(i for i,v in enumerate(g)if 8in v)
 return(g,g[a:b]+g[:a]+g[b:])[a<b]
p=lambda g:f(f(f(f(g))))