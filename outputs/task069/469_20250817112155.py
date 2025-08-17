def p(g):
 m=n=9;M=N=0
 for i in range(10):
  for j in range(10):
   if 0<g[i][j]!=8:
    m=min(m,i);n=min(n,j);M=max(M,i);N=max(N,j)
 G=[r[n:N+1]for r in g[m:M+1]]
 H=len(G);W=len(G[0])
 for i in range(11-H):
  for j in range(11-W):
   if all(g[i+I][j+J]>0and G[I][J]>0 or g[i+I][j+J]==G[I][J]==0 for I in range(H) for J in range(W)):
    for I in range(H):
     for J in range(W):g[i+I][j+J]=G[I][J]
 for i in range(m,M+1):
  for j in range(n,N+1):g[i][j]=0
 return g