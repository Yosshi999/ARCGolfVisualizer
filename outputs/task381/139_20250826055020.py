E=enumerate
def p(g):
 for v in g[1:9]:
  if sum(v)>3:
   l,*_,r=[j for j,x in E(v)if x]
   for j,x in E(v):v[j]=x or 9*(l<=j<=r)
 return g