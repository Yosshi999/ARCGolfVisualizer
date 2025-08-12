def p(g):
 for i in range(1,15):
  for j in range(1,15):
   if g[i-1][j-1]==g[i][j-1]==g[i-1][j]==8and g[i][j]==6:
    W=H=0
    while g[i+H][j]==6:H+=1
    while g[i][j+W]==6:W+=1
    for I in range(i,i+H):
     for J in range(j,j+W):
      if g[I][J]==8:g[I][J]=4
    for I in range(i-1,i+H+1):g[I][j-1]=g[I][j+W]=3
    for J in range(j-1,j+W+1):g[i-1][J]=g[i+H][J]=3
 return g