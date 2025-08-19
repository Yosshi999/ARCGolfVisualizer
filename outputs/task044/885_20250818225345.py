def p(g):
 o=[*map(list,g)];v=[];K=[];D=[0]*10;C=0
 for r in range(10):
  for c in range(10):
   if(x:=g[r][c]):
    if x*all(10>r+d>-1<c+e<10and g[r+d][c+e]!=x for d,e in[(-1,0),(1,0),(0,-1),(0,1)]):C=x
    D[x]+=1
   if(r,c)not in v and x==5:
    W=H=0
    while c+W<10and g[r][c+W]==5:W+=1
    while r+H<10and g[r+H][c]==5:H+=1
    m=n=10;M=N=-1
    for y in range(r,r+H):
     for z in range(c,c+W):
      if g[y][z]<1:m=min(m,y);n=min(n,z);M=max(M,y);N=max(N,z)
      v+=[(y,z)]
    K+=[(m,n,[R[n:N+1]for R in g[m:M+1]])]
 for m,n,k in K:
  h,w=len(k),len(k[0]);s=sum(v<1for u in k for v in u);t={i for i in range(10)if D[i]==s}-{0,5,C}
  for i in range(11-h):
   for j in range(11-w):
    if all((g[i+y][j+x]in t)==(k[y][x]<1)for y in range(h)for x in range(w)):
     for y in range(h):
      for x in range(w):
       if k[y][x]<1:o[m+y][n+x]=g[i+y][j+x];o[i+y][j+x]=0
 return o