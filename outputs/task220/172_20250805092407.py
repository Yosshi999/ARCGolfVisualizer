def p(g):
 r=range(len(g));R=[-1,0,1]
 for i in r:
  for j in r:
   if(c:=g[i][j])in[2,3,8]:
    for x in R:
     for y in R:g[i+x][j+y]=[c/2,6][c%2]
   g[i][j]=c
 return g