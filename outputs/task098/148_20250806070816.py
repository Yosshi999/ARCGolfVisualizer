e=enumerate
def p(g):
 for i,v in e(g):
  for j,w in e(v):
   if w and g[i-1][j]*g[i+1][j]*v[j-1]*v[j+1]:v[j]=16
 return[[w&15for w in v]for v in g]