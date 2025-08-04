def p(g):
 h,w=len(g),len(g[0])
 o=[r[:] for r in g]
 for r in range(h):
  for c in range(w):
   if g[r][c]==2:
    for dr in [-1,0,1]:
     for dc in [-1,0,1]:
      nr,nc=r+dr,c+dc
      if 0<=nr<h and 0<=nc<w and g[nr][nc]==0:
       o[nr][nc]=1
 return o