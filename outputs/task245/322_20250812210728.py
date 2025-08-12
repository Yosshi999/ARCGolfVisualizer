def p(g):
 h=[[0]*len(v)for v in g]
 m=n=30;u=v=30
 for i in range(len(g)):
  for j in range(len(g[0])):
   if g[i][j]==2:
    m=min(m,i);n=min(n,j)
   if g[i][j]==3:
    u=min(u,i);v=min(v,j)
 for i in range(len(g)):
  for j in range(len(g[0])):
   if g[i][j]==2:h[i+u-m+1][j+v-n+1]=2
   if g[i][j]==3:h[i][j]=3
 return h