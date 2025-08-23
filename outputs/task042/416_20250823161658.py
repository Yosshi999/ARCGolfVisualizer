def p(g):
 B=[0]
 for k in [3,2,1]:
  def f(G,B):
   for i in range(11-k*2):
    for j in range(11-k*2):
     if G[i][j]and sum(v==3for u in G[i:i+k*2]for v in u[j:j+k*2])==k*k*2:
      B[0]=1
      for I in range(k):
       for J in range(k):
        if 0<=(u:=i-k+I)<10>(v:=j+k*2+J)>=0:G[u][v]=8
        if 0<=(u:=i+k*2+I)<10>(v:=j-k+J)>=0:G[u][v]=8
   return [r[::-1]for r in G]
  g=f(f(g,B),B)
  if B[0]:return g