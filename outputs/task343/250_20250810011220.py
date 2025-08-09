def q(g,k):
 for i,r in enumerate(g):
  if sum(r)==0 or all([u==v for u,v in zip(r,g[i%k])]):
   g[i]=g[i%k]
  else:return 0
 return [*map(list,zip(*g))]
def p(g):
 g=[*map(list,zip(*g))]
 for k in range(3,9):
  if (h:=q([[*v]for v in g],k)):return h