def p(g):
 h=[[0]*11for _ in range(11)]
 for i in range(11):h[i][3]=h[i][7]=5
 for j in range(11):h[3][j]=h[7][j]=5
 for i in range(3):
  for j in range(3):
   G=[r[j*4:j*4+3]for r in g[i*4:i*4+3]]
   for u in range(3):
    for v in range(3):
     if G[u][v]==4:
      for y in range(3):
       for x in range(3):
        h[u*4+y][v*4+x]=G[y][x]
      return h