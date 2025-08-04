def p(g):
 h,w=len(g),len(g[0])
 o=[[0]*w for _ in range(h)]
 cross_r,cross_c=-1,-1
 cross_color=0
 offset=0
 for r in range(h):
  for c in range(w):
   if g[r][c]!=0 and g[r][c]!=5:
    cross_color=g[r][c]
    break
 for r in range(h):
  if all(g[r][c]==cross_color for c in range(w)):
   cross_r=r
   break
 for c in range(w):
  if all(g[r][c]==cross_color for r in range(h)) and c!=w-1:
   cross_c=c
   break
 for r in range(h):
  if g[r][w-1]==5:
   offset+=1
 for c in range(w):
  o[cross_r+offset][c]=cross_color
 for r in range(h):
  o[r][cross_c-offset]=cross_color
 return o