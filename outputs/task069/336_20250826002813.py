r=range
def p(g):
 X,Y=zip(*[(i,j)for i in r(10)for j in r(10)if g[i][j]%8])
 m=min(X);M=max(X);n=min(Y);N=max(Y)
 H=M-m+1;W=N-n+1
 for i in r(11-H):
  for j in r(11-W):
   if all((g[i+I][j+J]>0)==(g[m+I][n+J]>0)for I in r(H)for J in r(W)):
    for I in r(H):g[i+I][j:j+W]=g[m+I][n:n+W]
 for v in g[m:M+1]:v[n:N+1]=[0]*(N+1-n)
 return g