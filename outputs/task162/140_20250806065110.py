r=range(18)
def p(g):
 for i in r:
  for j in r:
   if max(max(u[j:j+3])for u in g[i:i+3])<1:
    for u in g[i:i+3]:u[j:j+3]=[1]*3
 return g