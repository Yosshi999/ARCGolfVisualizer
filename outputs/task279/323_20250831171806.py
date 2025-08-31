E=enumerate
def D(g,y,x):
 if len(g)>y>-1<x<len(g[0])>2>g[y][x]:
  g[y][x]=8
  for i,j in(y-1,x),(y,x-1),(y+1,x),(y,x+1):D(g,i,j)
def p(g):
 o=[[[]]*len(v)for v in g]
 for i,v in E(g):
  for j,x in E(v):
   if x<2:o[i][j]=[(i,j)]+([],o[i-1][j])[i>0]+([],o[i][j-1])[j>0]
   if len(o[i][j])>len({*o[i][j]}):D(g,i,j)
 return g