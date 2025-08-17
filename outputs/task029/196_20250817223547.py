e=enumerate
def p(g):
 for c in sum(g,[]):
  P=[(i,j)for i,v in e(g)for j,w in e(v)if w==c];i,j=min(P);k,l=max(P)
  if all((a-i)*(k-a)*(b-j)*(l-b)==0for a,b in P):return[v[j+1:l]for v in g[i+1:k]]