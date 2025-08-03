def p(g):
 h=[[0for _ in v]for v in g]
 for i in range(len(g)-1):
  for j in range(len(g[0])-1):
   if g[i][j]and g[i][j+1]and g[i+1][j]:I,J=i,j
   if g[i+1][j+1]and g[i+1][j]and g[i][j+1]:
    for u in range(I,i+1):
     for v in range(J,j+1):
      h[u][v+1]=g[u][v]
    h[i][j+1]=g[i][j+1]
    for v in range(J,j+2):h[i+1][v]=g[i+1][v]
 return h