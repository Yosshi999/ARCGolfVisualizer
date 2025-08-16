e=enumerate
def p(g):
 v,h=zip(*[(i,j)for i,v in e(g)for j,x in e(v)if x])
 u,*_,d=sorted(v)
 l,*_,r=sorted(h)
 for i in range(u,d+1):
  for j in range(l,r+1):
   if i in[u,d]or j in[l,r]:g[i][j]=[*({g[u][l],g[d][r]}-{0,8})][0]
   else:g[i][j]=[*({g[u+1][l+1],g[d-1][r-1]}-{0,8})][0]
 return g