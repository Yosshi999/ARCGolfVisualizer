E=enumerate
L=len
def p(g):
 o=[[[]]*(w:=L(v))for v in g]
 def D(y,x):
  if L(g)>y>-1<x<w>2>g[y][x]:g[y][x]=8;D(y-1,x);D(y+1,x);D(y,x-1);D(y,x+1)
 for i,v in E(g):
  for j,x in E(v):
   if x<2:o[i][j]=[(i,j)]+o[i-1][j]+o[i][j-1]
   if L(o[i][j])>L({*o[i][j]}):D(i,j)
 return g