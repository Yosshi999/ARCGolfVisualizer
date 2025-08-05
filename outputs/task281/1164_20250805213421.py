def p(g):
 h,w=len(g),len(g[0])
 o=[[g[r][c] for c in range(w)] for r in range(h)]
 
 # Find cyan pixel
 cyan_r=cyan_c=None
 for r in range(h):
  for c in range(w):
   if g[r][c]==8:
    cyan_r,cyan_c=r,c
    break
  if cyan_r is not None:break
 
 if cyan_r is None:return o
 
 # Find the box boundaries and colors
 box_r1=box_r2=box_c1=box_c2=None
 outer_color=inner_color=None
 
 for r in range(h):
  for c in range(w):
   if g[r][c]!=0 and g[r][c]!=8:
    if box_r1 is None:box_r1=box_r2=r;box_c1=box_c2=c
    else:box_r1=min(box_r1,r);box_r2=max(box_r2,r);box_c1=min(box_c1,c);box_c2=max(box_c2,c)
    if outer_color is None:outer_color=g[r][c]
 
 # Find inner color
 if box_r2>box_r1 and box_c2>box_c1:
  inner_color=g[box_r1+1][box_c1+1]
 
 # Remove cyan pixel
 o[cyan_r][cyan_c]=0
 
 # Extend box to cyan pixel
 new_r1,new_r2=min(box_r1,cyan_r),max(box_r2,cyan_r)
 new_c1,new_c2=min(box_c1,cyan_c),max(box_c2,cyan_c)
 
 # Draw extended box
 for r in range(new_r1,new_r2+1):
  for c in range(new_c1,new_c2+1):
   if r==new_r1 or r==new_r2 or c==new_c1 or c==new_c2:
    o[r][c]=outer_color
   elif inner_color is not None:
    o[r][c]=inner_color
 
 return o