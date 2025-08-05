def p(g):
 for i in range(1,len(g)-1):
  for j in range(1,len(g[0])-1):
   if g[i-1][j]*g[i+1][j]*min(g[i][j-1:j+2]):g[i][j]=2
 return g