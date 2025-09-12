e=enumerate
p=lambda g:[[v[j]or(0<sum([*map(max,*g)][:j])<4)*(2in v)*8|any(max(g[:i+1]))*any(max(g[i:]))*(3in w)*8for j,w in e(zip(*g))]for i,v in e(g)]