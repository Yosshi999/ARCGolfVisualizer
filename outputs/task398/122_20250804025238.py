def p(g):
 t=len(set(g[0])-{0})
 r=range(5*t-1)
 h=[g[0]+[0]*~-t*5]
 for _ in r:
  h=[[0]+[h[0][i]for i in r]]+h
 return h