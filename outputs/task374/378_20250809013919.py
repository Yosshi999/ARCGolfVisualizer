def p(g):
 X=[]
 for i in range(10):
  for j in range(10):
   if g[i][j]==5:
    if i>0and g[i-1][j]>9:g[i][j]=g[i-1][j]+10
    elif j>0and g[i][j-1]>9:g[i][j]=g[i][j-1]+10
    else:
     g[i][j]=10+len(X);X.append(0)
    X[g[i][j]%10]+=1
 Y=[X.index(c)for c in sorted(X)]
 for i in range(10):
  for j in range(10):
   if g[i][j]>0:g[i][j]=[2,4,1][Y.index(g[i][j]%10)]
 return g