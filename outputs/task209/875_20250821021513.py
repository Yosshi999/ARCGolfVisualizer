def p(g):
 m=n=30;M=N=0
 for i in range(len(g)):
  for j in range(len(g[0])):
   if g[i][j]==4:
    m=min(m,i);n=min(n,j);M=max(M,i);N=max(N,j)
 H=[[*r[n:N+1]]for r in g[m:M+1]]
 for i in range(m,M+1):
  for j in range(n,N+1):g[i][j]=0
 m=n=30;M=N=0
 for i in range(len(g)):
  for j in range(len(g[0])):
   if g[i][j]>0:
    m=min(m,i);n=min(n,j);M=max(M,i);N=max(N,j)
 G=[r[n:N+1]for r in g[m:M+1]]
 hs={}
 for k in [4,3,2,1]:
  for i in range(len(H)+1-len(G)*k):
   for j in range(len(H[0])+1-len(G[0])*k):
    h=[[*r]for r in H];b=1;c=0
    for u in range(len(G)):
     for v in range(len(G[0])):
      S=set(h[i+u*k+I][j+v*k+J]for I in range(k)for J in range(k))
      if len(S)>1 or 0!=[*S][0]!=G[u][v]:
       b=0;break
      if [*S][0]!=0:c+=1
      for I in range(k):
       for J in range(k):h[i+u*k+I][j+v*k+J]=G[u][v]
    if b and c:hs[(k,c)]=h
 return hs[max(hs)]