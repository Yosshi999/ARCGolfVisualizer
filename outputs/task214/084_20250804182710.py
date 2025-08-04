def p(g):
 for i in[0,1,2]:
  for j in[0,1,2]:g[j][6-i]=g[2-i][~j]=g[i][j]
 return g