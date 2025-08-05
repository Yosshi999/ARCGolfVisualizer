def p(g):
 h,w=len(g),len(g[0])
 o=[[0]*w for _ in range(h)]
 start_col=-1
 color=0
 for c in range(w):
  if g[h-1][c]>0:
   start_col=c
   color=g[h-1][c]
   break
 if start_col==-1:return o
 col=start_col
 row=h-1
 up=True
 while col<w:
  o[row][col]=color
  if up:
   for r in range(row-1,-1,-1):
    o[r][col]=color
   row=0
  else:
   for r in range(row+1,h):
    o[r][col]=color
   row=h-1
  up=not up
  col+=1
  if col<w:
   o[row][col]=5
   col+=1
 return o