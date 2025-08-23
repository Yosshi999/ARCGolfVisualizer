def p(g):
 h=[*map(list,g)]
 for i in range(12):
  for j in range(12):
   if g[i][j]==5:
    K=0
    while j+K<12and g[i][j+K]:K+=1
    for I in range(i,i+K):
     for J in range(j,j+K):
      h[I][J]=g[I][J]or K+3;g[I][J]=0
 return h