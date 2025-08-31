def f(g):
 for v in[v for v in g if len({*v})>2][1:-1]:
  for j in range(10):v[j]|=8*any(v[:j])*any(v[j:])*(v[j]<1)
 return[*map(list,zip(*g))]
p=lambda g:f(f(g))