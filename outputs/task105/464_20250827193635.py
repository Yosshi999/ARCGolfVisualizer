e=enumerate
def p(g):
 h=[*map(list,g)]
 I,J=zip(*[(i,j)for i,v in e(g)for j,w in e(v)if w])
 m=min(I);M=max(I);n=min(J);N=max(J)
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