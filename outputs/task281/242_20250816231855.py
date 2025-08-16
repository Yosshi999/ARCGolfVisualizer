e=enumerate
def p(g):
 v,h=zip(*[(i,j)for i,v in e(g)for j,x in e(v)if x]);u,*_,d=sorted(v);l,*_,r=sorted(h)
 for i in range(u,d+1):
  for j in range(l,r+1):b=1-(i in[u,d]or j in[l,r]);g[i][j]=[*({g[u+b][l+b],g[d-b][r-b]}-{0,8})][0]
 return g