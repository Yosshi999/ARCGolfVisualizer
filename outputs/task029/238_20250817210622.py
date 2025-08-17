e=enumerate
def p(g):
 for c in sum(g,[]):
  p=[(i,j)for i,v in e(g)for j,w in e(v)if w==c]
  i,j=min(p)
  k,l=max(p)
  h=[v[:j]+v[j+1:l]+v[l+1:]for v in g[:i]+g[i+1:k]+g[k+1:]]
  if sum(h,[]).count(c)==0:return[v[j+1:l]for v in g[i+1:k]]