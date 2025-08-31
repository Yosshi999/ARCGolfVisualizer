def p(g):
 for i in 0,3,6:
  for j in 4,7,10:
   for k in[0,1,2]*g[i+1][j+1]:g[i+k][j:j+3]=g[k][:3]
 return g