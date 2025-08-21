r=range(1,6)
def p(g):
 h=[v+[0]*3for v in g]+[[0]*6for _ in g]
 for i in r:
  for j in r:h[i][j]=h[i][j]or h[i-1][j-1]
 return h