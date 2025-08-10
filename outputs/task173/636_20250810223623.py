def p(g):
 H=[]
 for i in range(len(g)-2):
  for j in range(len(g[0])-2):
   if g[i+1][j+1]>0and set([*g[i][j:j+3],g[i+1][j],g[i+1][j+2],*g[i+2][j:j+3]])!={0} and all(v[j]==v[j+2]for v in g[i:i+3]) and all(g[i][j+v]==g[i+2][j+v]for v in [0,1,2]):
    H+=[[u[j:j+3]for u in g[i:i+3]]]
 for h in H:
  for i in range(len(g)-2):
   for j in range(len(g[0])-2):
    K=set()
    for u in range(3):
     for v in range(3):
      if g[i+u][j+v]>0 and g[i+u][j+v]!=h[u][v]:K.add(0)
      if h[u][v]>0 and g[i+u][j+v]==0:K.add(h[u][v])
    if 0 not in K and len(K)==1:
     for u in range(3):
      for v in range(3):g[i+u][j+v]=h[u][v]
 return g