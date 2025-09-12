e=enumerate
p=lambda g:[[v[j]or(0<sum([*map(max,*g)][:j])<9)*(2in v)*4|any(max(g[:i+1]))*any(max(g[i:]))*(8in w)*4for j,w in e(zip(*g))]for i,v in e(g)]