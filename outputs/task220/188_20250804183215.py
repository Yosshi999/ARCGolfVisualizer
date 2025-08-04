def p(g):
 for i in range(len(g)):
  for j in range(len(g[0])):
   c=g[i][j]
   if c in[2,3,8]:
    for x in[-1,0,1]:
     for y in[-1,0,1]:g[i+x][j+y]=[c/2,6][c%2]
    g[i][j]=c
 return g