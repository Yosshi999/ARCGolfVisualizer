def p(g):
 Y=[]
 for i in range(len(g)):
  if g[i][0]==2:
   if Y and X==0:break
   X=-1;Y+=[8 in g[i]]
   if Y[-1]:
    for j in range(1,g[i].index(8)+1):g[i][j]=-g[i][j]//2+8
  if g[i][-1]==2:
   if Y and X!=0:break
   X=0;Y+=[8 in g[i]]
   if Y[-1]:
    for j in range(g[i].index(8),len(g[0])-1):g[i][j]=-g[i][j]//2+8
  if Y and sum(g[i])==0:break
 for I in range(i,len(g)):
  if g[I][X]==2:
   c=Y.pop(0)
   if c:
    for j in range(len(g[0])):g[I][j]=g[I][j]or 8
 return g