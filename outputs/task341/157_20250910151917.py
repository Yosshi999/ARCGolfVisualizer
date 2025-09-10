def f(g):
 for v in[v for v in g if len({*v})>2][1:-1]:v[:]=[v[j]or 8*any(v[:j])*any(v[j:])for j in range(10)]
 return[*map(list,zip(*g))]
p=lambda g:f(f(g))