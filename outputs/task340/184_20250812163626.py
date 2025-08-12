f=lambda g:[*map(list,zip(*[[m:=v[0],v[1]+(m if m in v[1:]else 0)]+v[2:]for v in g]))][::-1]
p=lambda g:(g:=f(f(f(f(g)))),g[:2]+[v[:2]+[0]*(len(v)-4)+v[-2:]for v in g[2:-2]]+g[-2:])[1]