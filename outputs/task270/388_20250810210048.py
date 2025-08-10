def p(g):
 h=[*zip(*g)]
 for i in range(15):
  for j in range(15):
   for c,d in [(1,7),(2,3)]:
    if g[i][j]==c:
     if d in g[i][j:]:
      g[i][j+g[i][j:].index(d)]=0;g[i][j+1]=d
     if d in g[i][:j]:
      g[i][g[i].index(d)]=0;g[i][j-1]=d
     if d in h[j][i:]:
      g[i+h[j][i:].index(d)][j]=0;g[i+1][j]=d
     if d in h[j][:i]:
      g[h[j].index(d)][j]=0;g[i-1][j]=d
 return g