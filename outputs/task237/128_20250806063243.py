e=enumerate
def p(g):
 for v in g:
  for j,_ in e(v):v[j]=max(v[:j+1])
 for i,v in e(g):
  if v[-1]<1:v[-1]=g[i-1][-1]
 return g