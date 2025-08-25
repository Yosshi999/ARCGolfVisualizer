def p(g):
 def D(y,x):
  if len(g[0])>x>-1<y<len(g)>0==(c:=g[y][x]):g[y][x]=3;return[(y,x)]+D(y,x-1)+D(y,x+1)+D(y-1,x)+D(y+1,x)
  return[]
 for K in [3,4,5]:
  if g[K][K]or g[K][0]or g[0][K]:break
 for i in range(len(g)):
  for j in range(len(g[0])):
   if g[i][j]==0:
    x=D(i,j)
    if len(x)!=K*K:
     for I,J in x:g[I][J]=4
 return g