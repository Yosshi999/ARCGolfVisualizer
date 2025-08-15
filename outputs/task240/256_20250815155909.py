def p(g):
 for i in range(19):
  for j in range(19):
   g[i][j]=g[i][j]or g[18-i][j]or g[i][18-j]or g[18-i][18-j]
 for k in range(3):
  if (c:=g[1+2*k][3+2*k]):
   for i in range(3+2*k,16-2*k,2):g[i][1+2*k]=g[1+2*k][i]=g[i][17-2*k]=g[17-2*k][i]=c
 return g