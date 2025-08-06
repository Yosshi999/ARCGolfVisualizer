def T(g,i,j,k):
 for I in range(i,i+k+1):
  if g[I][j]!=5:return 0
  if g[I][j+k]!=5:return 0
 for J in range(j,j+k+1):
  if g[i][J]!=5:return 0
  if g[i+k][J]!=5:return 0
 return all(v<5for u in g[i+1:i+k] for v in u[j+1:j+k])
def p(g):
 for i in range(12):
  for j in range(12):
   for k in range(1,12):
    if i+k<12 and j+k<12 and T(g,i,j,k):
     for I in range(i,i+k):
      for J in range(j,j+k):
       if g[I][J]==0:g[I][J]=2
 return g