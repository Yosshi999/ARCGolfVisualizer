def p(g,d=range(-2,3),E=enumerate):
 x=[r[:]for r in g]
 [x[i+a].__setitem__(j+b,v if abs(a)==abs(b)else r[j-1])
  for i,r in E(g)
  for j,v in E(r)if v and r[j-1]*r[j+1]
  for a in d for b in d if abs(a)==abs(b)or not a*b]
 return x