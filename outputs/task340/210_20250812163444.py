t=lambda g:[*map(list,zip(*g))][::-1]
f=lambda g:[[v[0],v[1]+(v[0]if v[0]in v[1:]else 0)]+v[2:]for v in g]
p=lambda g:(g:=t(f(t(f(t(f(t(f(g)))))))),g[:2]+[v[:2]+[0]*(len(v)-4)+v[-2:]for v in g[2:-2]]+g[-2:])[1]