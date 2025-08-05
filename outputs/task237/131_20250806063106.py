def p(g):
 for v in g:
  for j in range(len(v)):v[j]=max(v[:j+1])
 for i,v in enumerate(g):
  if v[-1]<1:v[-1]=g[i-1][-1]
 return g