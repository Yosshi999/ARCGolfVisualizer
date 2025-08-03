def p(g):
 h,w=len(g),len(g[0]);s=set()
 for r in range(h):
  for c in range(w):
   if g[r][c]:s.add(g[r][c])
 m=max(s)
 for r in range(h):
  for c in range(w):
   if g[r][c]<1:
    g[r][c]=(r*c)%m+1
 return g