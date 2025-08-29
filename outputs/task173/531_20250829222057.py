def p(g):
 H=[]
 for i in range(len(g)-2):
  for j in range(len(g[0])-2):
   G=sum(Q:=[u[j:j+3]for u in g[i:i+3]],[])
   if g[i+1][j+1]>0and G.count(0)in{6,4}and len(set(G))==3:H+=[Q]
 for h in H:
  for i in range(len(g)-2):
   for j in range(len(g[0])-2):
    K=set()
    for u in range(3):
     for v in range(3):
      if g[i+u][j+v]>0 and g[i+u][j+v]!=h[u][v]:K|={0}
      if h[u][v]>0 and g[i+u][j+v]==0:K|={h[u][v]}
    if 0not in K and len(K)==1:
     for u in range(3):
      for v in range(3):g[i+u][j+v]=h[u][v]
 return g