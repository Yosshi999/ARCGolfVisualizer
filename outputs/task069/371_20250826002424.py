r=range
def p(g):
 m=n=9;M=N=0
 for i in r(10):
  for j in r(10):
   if g[i][j]%8:m=min(m,i);n=min(n,j);M=max(M,i);N=max(N,j)
 G=[r[n:N+1]for r in g[m:M+1]]
 H=len(G);W=len(G[0])
 for i in r(11-H):
  for j in r(11-W):
   if all((g[i+I][j+J]>0)==(G[I][J]>0)for I in r(H)for J in r(W)):
    for I in r(H):g[i+I][j:j+W]=G[I]
 for v in g[m:M+1]:v[n:N+1]=[0]*(N+1-n)
 return g