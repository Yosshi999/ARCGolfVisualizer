f=lambda g:[[*map(min,*[w for w in g if{*v}-{0}=={*w}-{0}])]for v in g]
p=lambda g:2>len({*g[0]}-{0})and f(g)or[*zip(*f([*zip(*g)]))]