def p(g):
 B=g[0][0];f=sum(g,[]);C=max({*f}-{B},key=f.count);V=0
 H=[(i+1,j+1)for i in range(28)for j in range(28)if g[i+1][j+1]not in[B,C]and{g[i][j+1],g[i+1][j],g[i+1][j+2],g[i+2][j+1]}=={C}]
 for i in range(26):
  for j in range(26):
   if g[i+2][j+2]not in [B,C]:
    W=sum([C!=g[i+u][j+v]!=B for u,v in [(0,2),(2,0),(2,4),(4,2)]+[(u,v)for u in [1,2,3]for v in [1,2,3]]])
    if V<W:
     V=W;I,J=i+2,j+2
 for i,j in H:
  for u in [-1,0,1]:
   for v in [-1,0,1]:
    if g[I+u][J+v]!=B:g[i+u][j+v]=g[I+u][J+v]
  u=i-2
  while g[u][j]!=B and g[I-2][J]!=B:
   g[u][j]=g[I-2][J];u-=1
  u=i+2
  while g[u][j]!=B and g[I+2][J]!=B:
   g[u][j]=g[I+2][J];u+=1
  v=j-2
  while g[i][v]!=B and g[I][J-2]!=B:
   g[i][v]=g[I][J-2];v-=1
  v=j+2
  while g[i][v]!=B and g[I][J+2]!=B:
   g[i][v]=g[I][J+2];v+=1
 for u in range(I-2,I+3):
  for v in range(J-2,J+3):
   g[u][v]=B
 return g