def p(g):
 a=b=30;A=B=0
 for i in range(len(g)):
  for j in range(len(g[0])):
   if g[i][j]==5:
    a=min(a,i);b=min(b,j);A=max(A,i);B=max(B,j)
   elif g[i][j]>0:C=g[i][j]
 for i in range(a+1,A):g[i][b+1]=g[i][B-1]=C
 for j in range(b+1,B):g[a+1][j]=g[A-1][j]=C
 return g