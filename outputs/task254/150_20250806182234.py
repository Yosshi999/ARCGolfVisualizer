def p(g):
 s=[v.count(5)for v in zip(*g)]
 return[[(w>0)*((j==s.index(min(filter(None,s))))*2+(j==s.index(max(s))))for j,w in enumerate(v)]for v in g]