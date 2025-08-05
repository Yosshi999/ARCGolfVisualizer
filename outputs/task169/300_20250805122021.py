r=range(10)
def p(g):
 g=[[(g[i][j]>1)<<(10*i+j)for j in r]for i in r]
 for _ in r:
  for i in r:
   for j in r:
    if i and (a:=g[i][j])*(b:=g[i-1][j]):g[i][j]=g[i-1][j]=a|b
    if j and (a:=g[i][j])*(c:=g[i][j-1]):g[i][j]=g[i][j-1]=a|c
 return[[5-b if(b:=w.bit_count())else 0for w in v]for v in g]