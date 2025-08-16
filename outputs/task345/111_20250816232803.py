def p(g):
 for v,w in zip(g[::-1],g[8::-1]):
  for j in range(10):
   if v[j]&2:v[k:=j+w[j]%2]=w[k]=2
 return g