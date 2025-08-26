E=enumerate
def p(g):
 (u,l),*_,(d,r)=[(i+1,j+1)for i,v in E(g)for j,w in E(v)if w]
 for y,j,J in(0,l,r),(0,r-2,l-2),(2,r,l),(2,l-2,r-2):g[u-y][j],g[d-y][J]=g[d-y][J],g[u-y][j]
 return g