def p(g):
 h=[*map(list,zip(*g))]
 s=[v.count(5)for v in h]
 M,m=max(s),min([9if v<1else v for v in s])
 return[[(w>0)*((j==s.index(m))*2+(j==s.index(M)))for j,w in enumerate(v)]for v in g]