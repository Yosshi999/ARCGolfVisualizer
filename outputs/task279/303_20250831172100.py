E=enumerate
def p(g):
 o=[[[]]*(w:=len(v))for v in g]
 def D(y,x):
  if len(g)>y>-1<x<w>2>g[y][x]:g[y][x]=8;D(y-1,x);D(y+1,x);D(y,x-1);D(y,x+1)
 for i,v in E(g):
  for j,x in E(v):
   if x<2:o[i][j]=[(i,j)]+o[i-1][j]+o[i][j-1]
   if len(o[i][j])>len({*o[i][j]}):D(i,j)
 return g