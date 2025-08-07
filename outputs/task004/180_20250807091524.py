def p(g,E=enumerate):
 o=[[0]*len(g[0])for _ in g]
 for v in{*sum(g,[])}:
  P=[(i,j)for i,r in E(g)for j,x in E(r)if x==v];b,m=max(P)
  for i,j in P:o[i][j+(i<b)*(j<m)]=v
 return o