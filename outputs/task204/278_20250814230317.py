R=range
E=enumerate
def p(g):
 H=range(len(g))
 for N in H:
  for u,d in zip(H,H[N+1:]):
   for l,r in zip(H,H[N+1:]):
    if all(x==(I*(N+1-I)*J*(N+1-J)<1)for I,v in E(g[u:d+1])for J,x in E(v[l:r+1])):
     for I in R(u+1,d):
      for J in R(l+1,r):g[I][J]=5*(N&1)+2
 return g