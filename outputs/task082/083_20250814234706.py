def p(g):
 for i,v in enumerate(g[0]):
  if v:g[1][i-1:i+2]=[v,0,v]
 return g[:2]*3