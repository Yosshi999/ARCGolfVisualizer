def f(g,h,G):
 for k in [3,2,1]:
  for i in range(len(g)+1-k*3):
   for j in range(len(g[0])+1-k*3):
    if set([g[i+I][j+J]for I in range(k)for J in range(k)])=={G[0][0]}and set([g[i+k*2+I][j+k*2+J]for I in range(k)for J in range(k)])=={G[2][2]}:
     for u in range(3):
      for v in range(3):
       for I in range(k):
        for J in range(k):
         h[i+u*k+I][j+v*k+J]=G[u][v]
         g[i+u*k+I][j+v*k+J]=0
def p(g):
 for i in range(len(g)-2):
  for j in range(len(g[0])-2):
   G=[r[j:j+3]for r in g[i:i+3]]
   if len(set(sum(G,[])))==4:
    if G[0][0]==G[2][2]:G=[r[::-1]for r in G]
    H=G
 h=[[*r]for r in g]
 for i in [0,1]:
  for j in [0,1]:
   f(g,h,H);g=[r[::-1]for r in g];h=[r[::-1]for r in h]
  g=g[::-1];h=h[::-1]
 return h