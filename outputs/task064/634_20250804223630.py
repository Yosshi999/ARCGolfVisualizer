def C(g,i,j,u,v,b,c):
 if g[i][j]not in [b,c]:return True
 if i+u<0 or i+u>=len(g):return False
 if j+v<0 or j+v>=len(g[0]):return False
 if C(g,i+u,j+v,u,v,b,c):
  g[i][j]=c;return True
def p(g):
 c=0
 for i in range(len(g)):
  for j in range(len(g[0])):
   if (i<1 or g[i][j]!=(k:=g[i-1][j])) and (j<1 or g[i][j]!=(k:=g[i][j-1])) and (i>=len(g)-1 or g[i][j]!=(k:=g[i+1][j])) and (j>=len(g[0])-1 or g[i][j]!=(k:=g[i][j+1])):
    c=g[i][j];b=k
 for i in range(len(g)):
  for j in range(len(g[0])):
   if g[i][j]!=b and c<0:c=g[i][j]
   if g[i][j]==c:
    C(g,i,j,-1,0,b,c);C(g,i,j,1,0,b,c);C(g,i,j,0,-1,b,c);C(g,i,j,0,1,b,c)
 return g