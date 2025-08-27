def p(g):
 for k in range(49):
  i=k//7;j=k%7;h=[v[j:j+3]for v in g[i:i+3]]
  if all(4in v for v in h)and all(4in v for v in zip(*h)):
   for u in g[i:i+3]:
    for v in range(j,j+3):u[v]=u[v]or 7
 return g