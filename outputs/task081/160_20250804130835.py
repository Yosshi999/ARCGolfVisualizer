def p(g):
 for a in range(36):
  for k in[(i:=a//6),i+1]:
   for l in[(j:=a%6),j+1]:g[k][l]=max(g[k][l],sum(x for v in g[i:i+2]for x in v[j:j+2])//24)
 return g