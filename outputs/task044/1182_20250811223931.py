def f(g,i,j):
 W=H=0
 while j+W<10and g[i][j+W]==5:W+=1
 while i+H<10and g[i+H][j]==5:H+=1
 m=n=10;M=N=0
 for I in range(i,i+H):
  for J in range(j,j+W):
   if g[I][J]==0:
    m=min(m,I);n=min(n,J);M=max(M,I);N=max(N,J)
 return H,W,m,n,[r[n:N+1]for r in g[m:M+1]]
def p(g):
 C=0;K=[];H=[[*v]for v in g]
 D=[0]*10
 for i in range(10):
  for j in range(10):
   if g[i][j]>0:
    if (i==0 or g[i-1][j]!=g[i][j])and (j==0 or g[i][j-1]!=g[i][j])and (i==9or g[i+1][j]!=g[i][j])and (j==9or g[i][j+1]!=g[i][j]):C=g[i][j]
    D[g[i][j]]+=1
 for i in range(10):
  for j in range(10):
   if H[i][j]==5:
    h,w,m,n,k=f(g,i,j)
    K+=[(m,n,k)]
    for I in range(i,i+h):
     for J in range(j,j+w):H[I][J]=0
 H=[[*v]for v in g]
 for m,n,k in K:
  s=sum(v==0for u in k for v in u)
  c=[i for i in range(10) if D[i]==s and i not in{0,5,C}]
  for i in range(11-len(k)):
   for j in range(11-len(k[0])):
    B=1
    for I in range(len(k)):
     for J in range(len(k[0])):
      B&=g[i+I][j+J] in c and k[I][J]==0 or g[i+I][j+J]not in c and k[I][J]>0
    if B:
     for I in range(len(k)):
      for J in range(len(k[0])):
       if k[I][J]<1:
        H[m+I][n+J]=g[i+I][j+J];H[i+I][j+J]=0
 return H