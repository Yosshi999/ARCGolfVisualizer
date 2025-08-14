print('-'*20)
R=range
E=enumerate
def p(g):
 H=range(len(g))
 for N in H:
  for u,d in zip(H,H[N+1:]):
   for l,r in zip(H,H[N+1:]):
    if all(x==(I==0 or I==N+1 or J==0 or J==N+1)for I,v in E(g[u:d+1])for J,x in E(v[l:r+1])):
     print(f'box found -- ({u} {l}) ({u+N+1} {l+N+1})')
     for I in R(u+1,d):
      for J in R(l+1,r):g[I][J]=5*(N&1)+2
 return g