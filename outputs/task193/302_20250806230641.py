def p(g):
 h=[[0]*len(u)for u in g]
 for i in range(len(g)):
  for j in range(len(g[0])):
   for k in range(i+1,len(g)):
    for l in range(j+1,len(g[0])):
     if all(v>0 for u in g[i:k+1] for v in u[j:l+1]):
      for I in range(i,k+1):
       for J in range(j,l+1):
        h[I][J]=g[i][j]
 return h