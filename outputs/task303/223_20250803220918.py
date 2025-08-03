def p(g):
 h=[list(v)for v in g]
 for i,v in enumerate(g):
  if sum(v)==0:h[i]=[2]*len(v)
 h=[*map(list,zip(*h))]
 g=[*map(list,zip(*g))]
 for i,v in enumerate(g):
  if sum(v)==0:h[i]=[2]*len(v)
 return [*map(list,zip(*h))]