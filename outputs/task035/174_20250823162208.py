def p(g):
 s=sum(g,[]);P=max([x for x in s if x],key=s.count)
 def f(G):
  for r in G:
   if r[0]:r[r.index(P)]=r[0]
  return [*map(list,zip(*G))][::-1]
 return f(f(f(f(g))))