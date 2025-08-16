def p(g):
 for v,w in zip(g[::-1],g[-2::-1]):
  for j in range(10):
   if v[j]&2:k=j+w[j]%2;v[k]=w[k]=2
 return g