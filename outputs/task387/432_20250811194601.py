def p(g):
 B=[];C=[]
 for i in range(len(g)):
  for j in range(len(g[0])):
   if g[i][j]>0:
    B+=[(i,j)];C+=[g[i][j]]
 for k in range(4):
  i,j=B[k];c=C[(k+2)%4]
  for u in range(-1,2):
   for v in range(-1,2):
    if u or v:g[i+u][j+v]=c
 i,j,k,l,m,n=(*B[0],*B[1],*B[2])
 W=j+l;H=i+m
 for I in range(i+2,H//2+1,2):g[I][j]=g[H-I][j]=g[I][l]=g[H-I][l]=5
 for J in range(j+2,W//2+1,2):g[i][J]=g[i][W-J]=g[m][J]=g[m][W-J]=5
 return g