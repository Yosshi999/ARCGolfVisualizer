def p(g):
 for i in range(len(g[0])):
  if sum(v[i]for v in g):
   for j in range(len(g)):
    if g[j][i]<1:g[j][i]=8
 return[v*2for v in g]*2