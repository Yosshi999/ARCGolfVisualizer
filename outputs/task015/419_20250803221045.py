def p(g):
 h,w=len(g),len(g[0])
 o=[row[:] for row in g]
 for r in range(h):
  for c in range(w):
   if g[r][c]==1:  # Orthogonal twinkler
    for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
     nr,nc=r+dr,c+dc
     if 0<=nr<h and 0<=nc<w:
      o[nr][nc]=7
   elif g[r][c]==2:  # Diagonal twinkler
    for dr,dc in [(1,1),(-1,1),(1,-1),(-1,-1)]:
     nr,nc=r+dr,c+dc
     if 0<=nr<h and 0<=nc<w:
      o[nr][nc]=4
 return o