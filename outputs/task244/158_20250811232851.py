def p(g):
 for K in range(6):
  if g[K][K]!=g[0][0]:break
 h=[]
 for i in range(0,len(g),K+1):
  h+=[[g[i][j]for j in range(0,len(g[0]),K+1)][::-1]]
 return h