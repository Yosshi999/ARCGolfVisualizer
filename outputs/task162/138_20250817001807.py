def p(g):
 for k in range(324):
  i=k//18;j=k%18
  if max(max(u[j:j+3])for u in g[i:i+3])<1:
   for u in g[i:i+3]:u[j:j+3]=[1]*3
 return g