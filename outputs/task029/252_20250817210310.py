e=enumerate
def p(g):
 for c in sum(g,[]):
  p=[(i,j)for i,v in e(g)for j,w in e(v)if w==c]
  i,j=min(p)
  k,l=max(p)
  h=[v[:j]+v[j+1:l]+v[l+1:]for v in g[:i]+g[i+1:k]+g[k+1:]]
  if c not in sum(h,[]):I=i;J=j;K=k;L=l
 return[v[J+1:L]for v in g[I+1:K]]