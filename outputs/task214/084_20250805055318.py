r=[0,1,2]
def p(g):
 for i in r:
  for j in r:g[j][6-i]=g[2-i][~j]=g[i][j]
 return g