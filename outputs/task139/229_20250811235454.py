def p(g):
 for i in range(7):
  for j in range(7):
   h=[v[j:j+3]for v in g[i:i+3]]
   if all(4 in v for v in h)and all(4 in v for v in zip(*h)):
    for u in range(i,i+3):
     for v in range(j,j+3):g[u][v]=g[u][v]or 7
 return g