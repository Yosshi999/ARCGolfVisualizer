def p(g):
 for i in range(10):
  q=0;f=0
  for j in range(10):
   if f and g[i][j]<1:f,q=0,j
   if f<1 and g[i][j]:
    f=1
    if q>0:
     for J in range(q,j):g[i][J]=9
   if f<1 and (i>0and g[i-1][j]==2 or i<9and g[i+1][j]==2):q=0
 return g