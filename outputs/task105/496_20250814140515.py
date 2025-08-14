def p(g):
 m=n=30;M=N=0;h=[[*v]for v in g]
 for i in range(len(g)):
  for j in range(len(g[0])):
   if g[i][j]>0:
    m=min(m,i);n=min(n,j);M=max(M,i);N=max(N,j)
 for j in range(n,N+1):
  h[m][j]=g[m][j]or 2
  h[M][j]=g[M][j]or 2
 for i in range(m,M+1):
  h[i][n]=g[i][n]or 2
  h[i][N]=g[i][N]or 2
 for i in range(m+1,M):
  if sum(g[i][n+1:N])>1:
   for j in range(n,N):h[i][j]=g[i][j]or 2
 for j,v in enumerate(zip(*g)):
  if sum(v[m+1:M])>1:
   for i in range(m,M):h[i][j]=g[i][j]or 2
 return h