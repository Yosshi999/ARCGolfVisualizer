def p(g):
 h,w=len(g),len(g[0])
 o=[[g[r][c] for c in range(w)] for r in range(h)]
 for r in range(h):
  for c in range(w):
   if g[r][c]==2:
    # Check if this red pixel is part of an olive (has neighboring reds)
    neighbors=[]
    for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
     nr,nc=r+dr,c+dc
     if 0<=nr<h and 0<=nc<w and g[nr][nc]==2:
      neighbors.append((nr,nc))
    
    if neighbors:
     # This is an olive - fill 3x3 area with green, keep red centers
     for dr in [-1,0,1]:
      for dc in [-1,0,1]:
       nr,nc=r+dr,c+dc
       if 0<=nr<h and 0<=nc<w and g[nr][nc]==0:
        o[nr][nc]=3
     for nr,nc in neighbors:
      for dr in [-1,0,1]:
       for dc in [-1,0,1]:
        nnr,nnc=nr+dr,nc+dc
        if 0<=nnr<h and 0<=nnc<w and g[nnr][nnc]==0:
         o[nnr][nnc]=3
 return o