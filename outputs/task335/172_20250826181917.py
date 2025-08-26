e=enumerate
p=lambda g:[[v[j]or (0<sum([*map(max,*g)][:j])<9)*(2in v)*4or (0<sum([*map(max,g)][:i])<9)*(8in w)*4or (2in v and 8in w)*4for j,w in e(zip(*g))]for i,v in e(g)]