def f(g,i,j,u,v,c):
 while 10>i>-1<j<10:g[i][j]=c;i+=u;j+=v
def p(g):
 for i in range(9):
  for j in range(9):g[i][j]and g[i+1][j]and(g[i][j+1]and f(g,i+2,j+2,1,1,g[i][j])or g[i+1][j+1]and f(g,i-1,j+2,-1,1,g[i][j]))or g[i][j+1]and g[i+1][j+1]and(g[i][j]and f(g,i+2,j-1,1,-1,g[i][j])or g[i+1][j]and f(g,i-1,j-1,-1,-1,g[i][j+1]))
 return g