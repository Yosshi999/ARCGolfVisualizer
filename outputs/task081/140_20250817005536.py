def p(g):
 for a in range(36):
  for v in g[(i:=a//6):i+2]:
   for l in[j:=a%6,j+1]:v[l]=v[l]or sum(g[i][j:j+2]+g[i+1][j:j+2])//24
 return g