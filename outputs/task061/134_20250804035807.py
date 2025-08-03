def p(g):
 h,w=len(g),len(g[0])
 for r in range(h):
  for c in range(w):
   if g[r][c]<1:
    g[r][c]=(r*c)%max(sum(g,[]))+1
 return g