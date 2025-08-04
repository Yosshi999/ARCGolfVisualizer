def p(g):
 f=0
 for i in range(len(g)):
  for j in range(1,len(g[0])):
   if f*g[i][j]==3:
    for x in[-1,0,1]:
     for y in[-1,0,1]:g[i+x][j+y]=2
    g[i][j]=3;return g
   if g[i][j-1:j+2]==[2,3,2]:
    for x in[-1,0,1]:
     for y in[-1,0,1]:g[i+x][j+y]=0
    g[i][j]=3
    f=1