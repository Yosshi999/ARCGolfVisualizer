def p(g):
 g=[*map(list,zip(*g))]
 for v in g[::3]:
  for j in range(len(v)):v[j]*=1.5
 return [*map(list,zip(*g))]