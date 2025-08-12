def p(g):
 for K in range(3,6):
  if g[K][K]or g[K][0]or g[0][K]:break
 for i in range(K,len(g),K+1):
  for j in range(len(g[0])):
   g[i][j]=g[i][j]or 4
 for j in range(K,len(g[0]),K+1):
  for i in range(len(g)):
   g[i][j]=g[i][j]or 4
 for _ in range(16):
  for i in range(len(g)):
   for j in range(len(g[0])):
    if g[i][j]==0:
     if i>0and g[i-1][j]==4or j>0and g[i][j-1]==4or i<len(g)-1and g[i+1][j]==4or j<len(g[0])-1and g[i][j+1]==4:g[i][j]=4
 for i in range(len(g)):
  for j in range(len(g[0])):
   g[i][j]=g[i][j]or 3
 return g