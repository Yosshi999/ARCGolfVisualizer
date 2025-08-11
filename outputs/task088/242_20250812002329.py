def p(g):
 C=0;m=n=30;M=N=0
 for i in range(len(g)):
  for j in range(len(g[0])):
   if g[i][j]>0:
    if C==0:C=g[i][j]
    if g[i][j]==C:
     m=min(m,i);n=min(n,j);M=max(M,i);N=max(N,j)
 return [[C*(v>0)for v in u[n+1:N]]for u in g[m+1:M]]