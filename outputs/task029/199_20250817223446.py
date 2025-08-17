e=enumerate
def p(g):
 for c in sum(g,[]):
  P=[(i,j)for i,v in e(g)for j,w in e(v)if w==c];i,j=min(P);k,l=max(P)
  if all(a==i or a==k or b==j or b==l for a,b in P):return[v[j+1:l]for v in g[i+1:k]]