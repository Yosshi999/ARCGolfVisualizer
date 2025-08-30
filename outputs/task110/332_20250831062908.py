R=range
E=enumerate
def p(g):
 W,*_=[K for K in R(1,29)if all(a*a*b==a*b*b for v in g for(a,b)in zip(v,v[K:]))]+[29]
 H,*_=[K for K in R(1,29)if all(a*a*b==a*b*b for(c,d)in zip(g,g[K:])for(a,b)in zip(c,d))]
 C={}
 for(i,v)in E(g):
  for(j,w)in E(v):
   if w:C[i%H,j%W]=w
 for(i,v)in E(g):
  for(j,w)in E(v):v[j]=C[i%H,j%W]
 return g