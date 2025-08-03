def p(g):
 h,w=len(g),len(g[0])
 o=[r[:] for r in g]
 vs=set()
 for r in range(h):
  for c in range(w):
   if g[r][c]>0:vs.add(g[r][c])
 if not vs:return o
 mv=max(vs)
 for r in range(h):
  for c in range(w):
   if g[r][c]==0:
    o[r][c]=(r*c)%mv+1
 return o