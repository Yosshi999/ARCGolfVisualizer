def p(g):
 s=sum(g,[]);P=max([x for x in s if x],key=s.count)
 for _ in[0]*4:
  for r in g:
   if r[0]:r[r.index(P)]=r[0]
  g=[*map(list,zip(*g))][::-1]
 return g