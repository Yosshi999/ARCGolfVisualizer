def p(g):
 for i in range(len(g)):
  for j in range(len(g[0])):
   if sum(v>0for u in g[max(0,i-1):i+2]for v in u[max(j-1,0):j+2])<2:g[i][j]=0
 return g