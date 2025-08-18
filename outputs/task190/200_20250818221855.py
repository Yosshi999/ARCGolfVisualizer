r=range(8)
def p(g):
 for _ in[0]*4:
  for i in r:
   for j in r:
    if g[i][j]*min(g[i+1][j+1:j+3]):
     d=0
     while min(i,j)>=d:g[i-d][j-d]=g[i][j];d+=1
  g=[*map(list,zip(*g[::-1]))]
 return g