e=enumerate
def p(g):
 G=sum(g,[]);d=max({*G}-{0},key=G.count)
 for i,v in e(g[1:]):
  for j,w in e(v[1:]):
   if~-(0 in v[j:j+2]+g[i][j:j+2]):v[j:j+2]=g[i][j:j+2]=[d,d]
 return[[w*(w==d)for w in v]for v in g]