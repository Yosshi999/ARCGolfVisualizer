def p(g):
 s=l=30;t=r=0
 for i in range(len(g)):
  for j in range(len(g[0])):
   if g[i][j]>1:l=min(l,j);r=max(r,j);s=min(s,i);t=max(t,i)
 return[[w*(w>1)for w in v[l:r+1]]for v in g[s:t+1]]