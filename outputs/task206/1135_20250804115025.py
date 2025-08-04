def p(g):
 h,w=len(g),len(g[0])
 o=[r[:] for r in g]
 
 # Find gray marker (5)
 marker_r=marker_c=-1
 for r in range(h):
  for c in range(w):
   if g[r][c]==5:
    marker_r,marker_c=r,c
    break
  if marker_r>=0:break
 
 if marker_r==-1:return o  # No marker found
 
 # Find all sprite pixels
 sprite_pixels=[]
 for r in range(h):
  for c in range(w):
   if g[r][c]>0 and g[r][c]!=5:
    sprite_pixels.append((r,c))
 
 if not sprite_pixels:return o
 
 # Find the sprite center by looking for the most connected pixel
 best_center=sprite_pixels[0]
 max_neighbors=0
 
 for r,c in sprite_pixels:
  # Count 8-connected neighbors that are also sprite pixels
  neighbors=0
  for dr in [-1,0,1]:
   for dc in [-1,0,1]:
    if (dr,dc)!=(0,0) and (r+dr,c+dc) in sprite_pixels:
     neighbors+=1
  if neighbors>max_neighbors:
   max_neighbors=neighbors
   best_center=(r,c)
 
 center_r,center_c=best_center
 
 # Copy sprite relative to center
 for r in range(h):
  for c in range(w):
   if g[r][c]>0 and g[r][c]!=5:
    dr,dc=r-center_r,c-center_c
    nr,nc=marker_r+dr,marker_c+dc
    if 0<=nr<h and 0<=nc<w:
     o[nr][nc]=g[r][c]
 
 return o