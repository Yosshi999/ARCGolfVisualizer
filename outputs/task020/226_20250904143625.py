def p(g):
 I,J=zip(*[(i,j)for i in range(10)for j in range(10)if g[i][j]])
 m=min(I)
 n=min(J)
 H=2*m+4;W=2*n+4
 for _ in"..":
  for i in range(m,m+5):
   for j in range(n,n+5):
    g[i][j]|=g[H-i][j]|g[j-n+m][i-m+n]
 return g