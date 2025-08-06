def p(g):
 g=[*map(list,zip(*g))]
 s=[v.count(5)for v in g]
 M,m=max(s),min([9if v<1else v for v in s])
 g[s.index(M)][9-M:M]=[1]*M
 g[s.index(m)][9-m:m]=[2]*m
 return[[w%5for w in v]for v in zip(*g)]