def p(g):
 h,w=len(g),len(g[0])
 o=[r[:]for r in g]
 
 # Find cyan magnet (2x2 region of color 8)
 cyan_pos=None
 for r in range(h-1):
  for c in range(w-1):
   if(g[r][c]==8 and g[r][c+1]==8 and 
      g[r+1][c]==8 and g[r+1][c+1]==8):
    cyan_pos=(r,c)
    break
  if cyan_pos:break
 
 if not cyan_pos:return o
 
 # Find red rectangle (color 2)
 red_pixels=[]
 for r in range(h):
  for c in range(w):
   if g[r][c]==2:
    red_pixels.append((r,c))
 
 if not red_pixels:return o
 
 # Find bounding box of red rectangle
 min_r=min(r for r,c in red_pixels)
 max_r=max(r for r,c in red_pixels)
 min_c=min(c for r,c in red_pixels)
 max_c=max(c for r,c in red_pixels)
 
 tall=max_r-min_r+1
 wide=max_c-min_c+1
 
 # Determine movement direction based on relative positions
 cyan_r,cyan_c=cyan_pos
 
 # Clear old red rectangle
 for r,c in red_pixels:
  o[r][c]=0
 
 # Calculate new position based on cyan magnet position
 if cyan_r>max_r:  # Cyan below red - move red down to just above cyan
  new_red_r=cyan_r-tall
  new_red_c=min_c
 elif cyan_r+1<min_r:  # Cyan above red - move red up to just below cyan
  new_red_r=cyan_r+2
  new_red_c=min_c
 else:  # Cyan to the side - move red horizontally
  new_red_r=min_r
  if cyan_c>max_c:  # Cyan to the right - move red right to just left of cyan
   new_red_c=cyan_c-wide
  else:  # Cyan to the left - move red left to just right of cyan
   new_red_c=cyan_c+2
 
 # Draw red rectangle at new position
 for r in range(tall):
  for c in range(wide):
   old_r,old_c=min_r+r,min_c+c
   if g[old_r][old_c]==2:
    new_r,new_c=new_red_r+r,new_red_c+c
    if 0<=new_r<h and 0<=new_c<w:
     o[new_r][new_c]=2
 
 return o