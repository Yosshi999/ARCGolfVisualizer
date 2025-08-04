def p(g):
 h,w=len(g),len(g[0])
 o=[r[:] for r in g]
 box_r,box_c=-1,-1
 color=0
 for r in range(h-1):
  for c in range(w-1):
   if g[r][c]>0 and g[r][c+1]>0 and g[r+1][c]>0 and g[r+1][c+1]>0:
    if g[r][c]==g[r][c+1]==g[r+1][c]==g[r+1][c+1]:
     box_r,box_c=r,c
     color=g[r][c]
     break
  if box_r>=0:break
 if box_r==-1:return o
 for dr,dc in [(-1,-1),(-1,1),(1,-1),(1,1)]:
  check_r=box_r+(2 if dr==1 else -1) if dr!=0 else box_r
  check_c=box_c+(2 if dc==1 else -1) if dc!=0 else box_c
  if 0<=check_r<h and 0<=check_c<w and g[check_r][check_c]==color:
   r,c=box_r+(1 if dr==1 else 0),box_c+(1 if dc==1 else 0)
   while 0<=r<h and 0<=c<w:
    o[r][c]=color
    r+=dr
    c+=dc
 return o