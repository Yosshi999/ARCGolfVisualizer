def p(g):
 S=sorted((-x*y,y,x)for x in range(1,9)for y in range(2,6))
 for _,y,x in S:
  for i in range(len(g)+1-y):
   for j in range(len(g[0])+1-x):
    if sum(v for u in g[i:i+y]for v in u[j:j+x])==0:
     for I in range(i,i+y):
      for J in range(j,j+x):g[I][J]=6
     return g