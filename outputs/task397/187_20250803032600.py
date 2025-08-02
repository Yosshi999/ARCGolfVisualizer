def p(g):
 for i in range(9):
  for j in range(9):
   h={g[i][j],g[i+1][j],g[i][j+1],g[i+1][j+1]}
   if not h&{0,3}:
    for k in range(len(h)):
     g[i+k+2][j]=g[i+k+2][j+1]=3
 return g