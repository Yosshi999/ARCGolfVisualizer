r=range(10)
def p(g):
 g=[[{10*i+j}if g[i][j]else {}for j in r]for i in r]
 for _ in r:
  for i in r:
   for j in r:
    if i and (a:=g[i][j])and(b:=g[i-1][j]):g[i][j]=g[i-1][j]=a|b
    if j and (a:=g[i][j])and(c:=g[i][j-1]):g[i][j]=g[i][j-1]=a|c
 return[[1+(len(w)==6)if w else 0for w in v]for v in g]