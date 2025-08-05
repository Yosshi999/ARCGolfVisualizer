def f(g):
 a=max(i for i,v in enumerate(g)if 2in v)+1
 b=min(i for i,v in enumerate(g)if 8in v)
 return[*map(list,zip(*(g,g[a:b]+g[:a]+g[b:])[a<b]))][::-1]
p=lambda g:f(f(f(f(g))))