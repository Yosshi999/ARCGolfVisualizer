def p(g):
 h,w=len(g),len(g[0])
 o=[r[:] for r in g]
 box_r1,box_r2,box_c1,box_c2=-1,-1,-1,-1
 for r in range(h):
  for c in range(w):
   if g[r][c]==2:
    if box_r1==-1:box_r1=r
    if box_c1==-1:box_c1=c
    box_r2=max(box_r2,r)
    box_c2=max(box_c2,c)
 if box_r1==-1:return o
 for r in range(h):
  for c in range(w):
   if g[r][c]==5:
    if r<box_r1:
     nr=box_r1+1+(box_r1-r-1)
     if nr<=box_r2-1 and box_c1<c<box_c2:
      o[nr][c]=5
      o[r][c]=0
    elif r>box_r2:
     nr=box_r2-1-(r-box_r2-1)
     if nr>=box_r1+1 and box_c1<c<box_c2:
      o[nr][c]=5
      o[r][c]=0
    elif box_r1<r<box_r2 and c<box_c1:
     nc=box_c1+1+(box_c1-c-1)
     if nc<=box_c2-1:
      o[r][nc]=5
      o[r][c]=0
    elif box_r1<r<box_r2 and c>box_c2:
     nc=box_c2-1-(c-box_c2-1)
     if nc>=box_c1+1:
      o[r][nc]=5
      o[r][c]=0
 return o