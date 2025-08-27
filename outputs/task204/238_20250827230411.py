E=enumerate
def p(g):
 H=range(len(g))
 for N in H:
  for d in H[N+1:]:
   for r in H[N+1:]:
    if all(x==(I*(N+1-I)*J*(N+1-J)<1)for I,v in E(g[d-N-1:d+1])for J,x in E(v[r-N-1:r+1])):
     for v in g[d-N:d]:v[r-N:r]=[N%2*5+2]*N
 return g