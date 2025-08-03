def p(g):
 h,w=len(g),len(g[0])
 o=[[0]*w for _ in range(h)]
 # Find colored cells
 cells=[(r,c,g[r][c]) for r in range(h) for c in range(w) if g[r][c]!=0]
 if len(cells)<2:return o
 # Determine if this was transposed by looking at the aspect ratio and pattern
 # If height > width, likely transposed (originally wide)
 transposed = h > w
 if transposed:
  # Work with transposed coordinates
  cells_t=[(c,r,color) for r,c,color in cells]
  cells_t.sort()
  r1,c1,color1=cells_t[0]
  r2,c2,color2=cells_t[1]
  # Create vertical stripes in transposed space
  start=min(c1,c2)
  sep=abs(c2-c1)-1 if c1!=c2 else 1
  colors=[color1,color2] if c1<=c2 else [color2,color1]
  color_idx=0
  for c in range(start,h,sep+1):
   for r in range(w):
    o[c][r]=colors[color_idx]
   color_idx=1-color_idx
 else:
  # Normal vertical stripes
  cells.sort(key=lambda x:x[1])  # Sort by column
  start=cells[0][1]
  colors=[cells[0][2],cells[1][2]]
  if len(cells)>=2:
   sep=cells[1][1]-cells[0][1]-1 if cells[1][1]!=cells[0][1] else 1
  else:
   sep=1
  color_idx=0
  for c in range(start,w,sep+1):
   for r in range(h):
    o[r][c]=colors[color_idx]
   color_idx=1-color_idx
 return o