def p(g):
 for _,y,x in sorted((-x*y,y,x)for x in range(9)for y in range(2,6)):
  for i in range(len(g)+1-y):
   for j in range(len(g[0])+1-x):
    if sum(sum(u[j:j+x])for u in g[i:i+y])<1:
     for v in g[i:i+y]:v[j:j+x]=[6]*x
     return g