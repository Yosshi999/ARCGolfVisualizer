def D(g,i,j,B,u,v):
 if g[i][j]>8:
  B[0]|=g[i][j]>9;return []
 g[i][j]+=10;x=[(i,j)]
 if i>0and (i-1,j)!=(u,v):x+=D(g,i-1,j,B,i,j)
 if j>0and (i,j-1)!=(u,v):x+=D(g,i,j-1,B,i,j)
 if i<len(g)-1and (i+1,j)!=(u,v):x+=D(g,i+1,j,B,i,j)
 if j<len(g[0])-1and (i,j+1)!=(u,v):x+=D(g,i,j+1,B,i,j)
 return x
def p(g):
 for i in range(len(g)):
  for j in range(len(g[0])):
   if g[i][j]==1:
    B=[0];x=D(g,i,j,B,-1,-1)
    for I,J in x:g[I][J]=11+7*B[0]
 return [[v%10for v in u]for u in g]