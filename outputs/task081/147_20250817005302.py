def p(g):
 for a in range(36):
  for k in[i:=a//6,i+1]:
   for l in[j:=a%6,j+1]:g[k][l]=g[k][l]or sum(sum(v[j:j+2])for v in g[i:i+2])//24
 return g