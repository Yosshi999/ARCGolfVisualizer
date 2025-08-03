def p(g):
 t=sum([c!=0 for c in g[0]])
 h=[g[0]+[0]*(5*t-5)]
 for _ in[0]*(5*t-1):
  h=[[0]+[h[0][i]for i in range(5*t-1)]]+h
 return h