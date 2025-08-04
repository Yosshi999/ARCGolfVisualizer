def p(g):
 h,w=len(g),len(g[0])
 o=[r[:] for r in g]
 for r in range(h):
  for c in range(w):
   if g[r][c]>0:
    color=g[r][c]
    for dr,dc in [(1,1),(1,-1)]:
     found=False
     for i in range(1,max(h,w)):
      nr,nc=r+i*dr,c+i*dc
      if 0<=nr<h and 0<=nc<w and g[nr][nc]==color:
       for j in range(1,i):
        fr,fc=r+j*dr,c+j*dc
        if 0<=fr<h and 0<=fc<w:
         o[fr][fc]=color
       found=True
       break
      elif not(0<=nr<h and 0<=nc<w):break
     if found:break
 return o