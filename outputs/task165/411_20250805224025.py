def K(g):
 k=[[0,1,0],[1,1,1],[1,0,1]]
 for i in range(18):
  for j in range(18):
   if all(g[i+I][j+J]>0 and k[I][J]>0 or k[I][J]==0 for I in range(3) for J in range(3)):
    return g[i][j+1]
def p(g):
 k=K(g)
 g=[*map(list,zip(*g))]
 for i in range(20):
  for j in range(20):
   if 0<g[i][j]!=k and k in g[i][:j]:
    n=g[i][::-1].index(k)
    g[i]=g[i][:-n]+[g[i][j]]*n
    break
 return [*map(list,zip(*g))]