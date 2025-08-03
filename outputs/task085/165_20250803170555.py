def p(g):
 for i in range(len(g)-2):
  for j in range(len(g[0])-2):
   c={v for u in g[i:i+3]for v in u[j:j+3]}
   if 0not in c and len(c)==1:g[i+1][j+1]=0
 return g