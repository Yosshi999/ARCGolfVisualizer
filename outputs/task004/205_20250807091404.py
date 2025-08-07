def p(g,E=enumerate):
 o=[[0]*len(g[0])for _ in g]
 for v in{*sum(g,[])}:
  P=[(i,j)for i,r in E(g)for j,x in E(r)if x==v]
  for i,j in P:o[i][j+(i<max(i for i,_ in P))*(j<max(j for _,j in P))]=v
 return o