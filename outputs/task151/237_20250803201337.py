def p(g):
 for i in range(len(g)-2):
  for j in range(len(g[0])-2):
   if sum([v>0for v in g[i+1][j:j+3]+[g[i][j+1],g[i+2][j+1]]])==5:
    g[i][j]=g[i][j+1]=g[i][j+2]=g[i+1][j]=g[i+1][j+2]=g[i+2][j]=g[i+2][j+1]=g[i+2][j+2]=4
    return g