e=enumerate
p=lambda g:[[v[j]or(0<sum([*map(max,*g)][:j])<9)*(2in v)*4|(0<sum([*map(max,g)][:i])<9)*(8in w)*4|(2in v)*(8in w)*4for j,w in e(zip(*g))]for i,v in e(g)]