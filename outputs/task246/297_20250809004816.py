def p(g):
 for i,v in enumerate(g):
  if 2 in v:R=i
 h=[*zip(*g)]
 for j,v in enumerate(h):
  if 3 in v:
   G=j
   for i in range(R,v.index(3)):g[i][j]=8
   for i in range(v.index(3)+1,R):g[i][j]=8
 for j in range(G,g[R].index(2)):g[R][j]=8
 for j in range(g[R].index(2)+1,G+1):g[R][j]=8
 return g