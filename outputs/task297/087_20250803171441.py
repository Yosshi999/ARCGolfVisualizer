def p(g):
 for i in range(2,len(g)):
  g[i]=[g[0][(i-2)%len(g[0])]]*len(g[0])
 return g