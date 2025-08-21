def p(g):
 I,J=zip(*[(i,j)for i in range(10)for j in range(10)if g[i][j]])
 m=min(I);M=max(I)
 n=min(J);N=max(J)
 H=M+m;W=N+n
 for i in range(m,M+1):
  for j in range(n,N+1):
   g[i][j]=g[i][j]or g[H-i][j]or g[i][W-j]or g[H-i][W-j]or g[j-n+m][i-m+n]or g[j-n+m][W-(i-m+n)]
 return g