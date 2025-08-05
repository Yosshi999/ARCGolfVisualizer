r=range(10)
def p(g):
 g=[[(g[i][j]>1)<<(10*i+j)for j in r]for i in r]
 for _ in r:
  for i in r:
   for j in r:
    if i and g[i][j]*g[i-1][j]:g[i][j]=g[i-1][j]=g[i][j]|g[i-1][j]
    if j and g[i][j]*g[i][j-1]:g[i][j]=g[i][j-1]=g[i][j]|g[i][j-1]
 return[[1+(b==6)if(b:=w.bit_count())else 0for w in v]for v in g]