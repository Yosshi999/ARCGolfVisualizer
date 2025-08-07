def t(g,i,j,u,v):
 for _ in range(30):
  i+=u;j+=v
  if 0<=i<len(g)and 0<=j<len(g[0]):
   if g[i][j]==0:g[i][j]=3
   if 0<=i+u<len(g)and g[i+u][j]==2:u=-u
   if 0<=j+v<len(g[0])and g[i][j+v]==2:v=-v
def f(g):
 g=[*map(list,zip(*g))]
 for j in range(len(g[0])-1):
  if g[0][j]==g[1][j+1]==8:t(g,0,j,1,1)
  if g[1][j]==g[0][j+1]==8:t(g,0,j+1,1,-1)
  if g[-1][j]==g[-2][j+1]==8:t(g,11,j,-1,1)
  if g[-2][j]==g[-1][j+1]==8:t(g,11,j+1,-1,-1)
 return g
p=lambda g:f(f(g))