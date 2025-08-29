def p(g):
 s=sum(g,[9]);P,F,B=[*{k:0for k in sorted(s,key=s.count)}][-3:]
 def f(G):
  for i,r in enumerate(G):
   if F in r:
    for _ in '..':
     if P in r[:r.index(F)]:
      for j in range(r.index(P),r.index(F)):r[j]=P
     r=r[::-1]
    G[i]=r
  return [*map(list,zip(*G))]
 return f(f(g))