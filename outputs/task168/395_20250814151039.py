def f(g,i,j,u,v,c):
 while 0<=i<10and 0<=j<10:
  g[i][j]=c;i+=u;j+=v
def p(g):
 for i in range(9):
  for j in range(9):
   if g[i][j]==g[i+1][j]==g[i][j+1]>0:f(g,i+2,j+2,1,1,g[i][j])
   if g[i][j]==g[i+1][j]==g[i+1][j+1]>0:f(g,i-1,j+2,-1,1,g[i][j])
   if g[i][j]==g[i][j+1]==g[i+1][j+1]>0:f(g,i+2,j-1,1,-1,g[i][j])
   if g[i+1][j]==g[i][j+1]==g[i+1][j+1]>0:f(g,i-1,j-1,-1,-1,g[i][j+1])
 return g