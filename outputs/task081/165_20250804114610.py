def p(g):
 r=range(6)
 for i in r:
  for j in r:
   for k in[i,i+1]:
    for l in[j,j+1]:g[k][l]=max(g[k][l],sum(x for v in g[i:i+2]for x in v[j:j+2])//24)
 return g