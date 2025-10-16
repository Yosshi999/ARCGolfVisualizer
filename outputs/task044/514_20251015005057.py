def p(g):
 for col in{*sum(g,[])}:
  L=[(i,j)for i in range(10)for j in range(10)if g[i][j]==col]
  I,J=zip(*L)
  a=min(I)
  c=max(I)
  b=min(J)
  d=max(J)
  flg=False
  for i in range(10):
   for j in range(10):
    if all((not 10>i+x>-1<j+y<10 or g[i+x][j+y]==5)==(not 10>a+x>-1<b+y<10 or g[a+x][b+y]!=col)for x in range(-1,c-a+2)for y in range(-1,d-b+2)):
     flg=True
     for v in g[i:i+c-a+1]:
      for k in range(d-b+1):
       v[j+k]=5*(v[j+k]==5)or col
  if flg:
   for i,j in L:
    g[i][j]=0
 return g