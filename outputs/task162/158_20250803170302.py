def p(g):
 for i in range(18):
  for j in range(18):
   if all([v==0for u in g[i:i+3]for v in u[j:j+3]]):
    for u in g[i:i+3]:u[j]=u[j+1]=u[j+2]=1
 return g