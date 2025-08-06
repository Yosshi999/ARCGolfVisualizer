e=enumerate
def p(g):
 s=l=30;t=r=0
 for i,v in e(g):
  for j,w in e(v):
   if w>1:l=min(l,j);r=max(r,j);s=min(s,i);t=max(t,i)
 return[[w*(w>1)for w in v[l:r+1]]for v in g[s:t+1]]