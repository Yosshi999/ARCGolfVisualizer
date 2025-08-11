def p(g):
 K=len(set(g[4]))+1
 h=[[0]*5*K for _ in range(5*K)]
 B=[]
 for i in range(5):
  for j in range(5):
   if g[i][j]>0:
    if i<4 and j<4:B+=[(i*K,j*K)]
    for k in range(K):
     for l in range(K):
      h[i*K+k][j*K+l]=g[i][j]
 i,j=B[0]
 while 0<i and 0<j:
  h[i-1][j-1]=2
  i-=1;j-=1
 i,j=B[1];j+=K;i-=1
 while 0<=i and j<4*K:
  h[i][j]=2;i-=1;j+=1
 i,j=B[2];j-=1;i+=K
 while i<4*K and j>=0:
  h[i][j]=2;i+=1;j-=1
 i,j=B[3];j+=K;i+=K
 while i<4*K and j<4*K:
  h[i][j]=2;i+=1;j+=1
 return h