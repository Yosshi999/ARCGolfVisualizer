f=lambda g:[[w*(max(g).count(w)==v.count(w))for w in v]for v in g]
p=lambda g:2>len({*g[0]}-{0})and[*zip(*f([*zip(*g)]))]or f(g)