e=enumerate
def p(g):
 for i,v in e(g):
  for j,w in e(v):
   if(w<1)*i*j*v[j-1]*g[i-1][j-1]*g[i-1][j]:v[j]=9
 return[[w//3for w in v]for v in g]