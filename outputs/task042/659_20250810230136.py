def p(g):
 for w in [1,2,3]:
  for i in range(11-w):
   for j in range(11-w):
    if all(v==3 for u in g[i:i+w] for v in u[j:j+w]):W=w
 for i in range(9):
  for j in range(9):
   if g[i][j]==g[i+1][j+1]==3and g[i+1][j]==g[i][j+1]==0:
    for u in range(W):
     for v in range(W):
      I,J=i+W+1+u,j-W-W+1+v
      if 0<=I<10and 0<=J<10:g[I][J]=8
      I,J=i-W-W+1+u,j+W+1+v
      if 0<=I<10and 0<=J<10:g[I][J]=8
   if g[i][j]==g[i+1][j+1]==0and g[i+1][j]==g[i][j+1]==3:
    for u in range(W):
     for v in range(W):
      I,J=i-W-W+1+u,j-W-W+1+v
      if 0<=I<10and 0<=J<10:g[I][J]=8
      I,J=i+W+1+u,j+W+1+v
      if 0<=I<10and 0<=J<10:g[I][J]=8
 return g