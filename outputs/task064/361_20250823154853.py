def p(g):
 C=[0]*9+[0.1]
 for i in range(len(g)):
  for j in range(len(g[0])):
   C[g[i][j]]+=1
 P,F,B=[C.index(x)for x in sorted(C)[-3:]]
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