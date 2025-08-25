import itertools as T
R=range
def p(g):
 o=[*map(list,g)];v=[]
 for r in R(10):
  for c in R(10):
   x=g[r][c]
   if(r,c)not in v and x==5:
    W=H=0;m=n=10;M=N=-1
    while c+W<10and g[r][c+W]==5:W+=1
    while r+H<10and g[r+H][c]==5:H+=1
    for y in R(r,r+H):
     for z in R(c,c+W):
      if g[y][z]<1:m=min(m,y);n=min(n,z);M=max(M,y);N=max(N,z)
      v+=[(y,z)]
    k=[R[n:N+1]for R in g[m:M+1]]
    h=M+1-m;w=N+1-n
    for i,j,C,y,x in T.product(R(11-h),R(11-w),range(10),R(h),R(w)):
     if all((g[i+y][j+x]==C)==(k[y][x]<1)for y in R(h)for x in R(w))and sum(k,[]).count(0)==sum(g,[]).count(C)and k[y][x]<1:o[m+y][n+x]=C;o[i+y][j+x]=0
 return o