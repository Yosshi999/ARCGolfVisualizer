e=enumerate
def p(g):
 G=sum(g,[])
 c,d=sorted({*G}-{0},key=G.count)
 for i,v in e(g[1:]):
  for j,w in e(v[1:]):
   if set(v[j:j+2]+g[i][j:j+2])=={c,d}:v[j:j+2]=g[i][j:j+2]=[d,d]
 return[[w*(w==d)for w in v]for v in g]