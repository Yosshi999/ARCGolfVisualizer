def p(g):
 for i in range(len(g)-2):
  for j in range(len(g[0])-2):
   if g[i][j]and len(set(g[i][j:j+3]+g[i+1][j:j+3:2]+g[i+2][j:j+3]))==1:return[[g[i+1][j+1]]]