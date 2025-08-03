def p(g):
 h,w=len(g),len(g[0])
 o=[row[:] for row in g]
 # Find the center by looking for a cell with the most surrounding patterns
 center=None
 max_neighbors=0
 for r in range(2,h-2):
  for c in range(2,w-2):
   if g[r][c]>0:
    neighbors=sum(1 for dr,dc in [(-1,-1),(-1,1),(1,-1),(1,1),(-2,0),(0,2),(2,0),(0,-2),(-2,-2),(-2,2),(2,-2),(2,2)] if 0<=r+dr<h and 0<=c+dc<w and g[r+dr][c+dc]>0)
    if neighbors>max_neighbors:
     max_neighbors=neighbors
     center=(r,c)
 
 if not center:return o
 r,c=center
 
 # Extract colors from existing pattern
 colors=[g[r][c],0,0,0]  # center color
 # Radius 1 diagonal
 for dr,dc in [(-1,-1),(-1,1),(1,-1),(1,1)]:
  if 0<=r+dr<h and 0<=c+dc<w and g[r+dr][c+dc]>0:
   colors[1]=g[r+dr][c+dc]
   break
 # Radius 2 orthogonal
 for dr,dc in [(-2,0),(0,2),(2,0),(0,-2)]:
  if 0<=r+dr<h and 0<=c+dc<w and g[r+dr][c+dc]>0:
   colors[2]=g[r+dr][c+dc]
   break
 # Radius 3 far diagonal
 for dr,dc in [(-2,-2),(-2,2),(2,-2),(2,2)]:
  if 0<=r+dr<h and 0<=c+dc<w and g[r+dr][c+dc]>0:
   colors[3]=g[r+dr][c+dc]
   break
 
 # Fill in missing pieces
 radius_1=[(-1,-1),(-1,1),(1,-1),(1,1)]
 radius_2=[(-2,0),(0,2),(2,0),(0,-2)]
 radius_3=[(-2,-2),(-2,2),(2,-2),(2,2)]
 
 if colors[1]:
  for dr,dc in radius_1:
   if 0<=r+dr<h and 0<=c+dc<w:
    o[r+dr][c+dc]=colors[1]
 if colors[2]:
  for dr,dc in radius_2:
   if 0<=r+dr<h and 0<=c+dc<w:
    o[r+dr][c+dc]=colors[2]
 if colors[3]:
  for dr,dc in radius_3:
   if 0<=r+dr<h and 0<=c+dc<w:
    o[r+dr][c+dc]=colors[3]
 
 return o