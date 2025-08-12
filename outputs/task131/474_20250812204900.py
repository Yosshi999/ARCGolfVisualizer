def f(g):
 R=-1;m=30;M=0
 for i,v in enumerate(g):
  if all(u==2for u in v):R=i
  if 3in v:
   m=min(m,i);M=max(M,i)
 if R>=0:
  if R<m:
   for u in range(M-m+1):
    for j in range(len(g[0])):
     g[R+1+u][j]=g[m+u][j];g[m+u][j]=0
   for j in range(len(g[0])):g[R+M-m+2][j]=8
  else:
   for u in range(M-m+1):
    for j in range(len(g[0])):
     g[R-1-u][j]=g[M-u][j];g[M-u][j]=0
   for j in range(len(g[0])):g[R-M+m-2][j]=8
 return [*map(list,zip(*g))]
p=lambda g:f(f(g))