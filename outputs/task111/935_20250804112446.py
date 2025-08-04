def p(g):
 h,w=len(g),len(g[0])
 
 # Find the gray marker (5)
 marker_r,marker_c=-1,-1
 for r in range(h):
  for c in range(w):
   if g[r][c]==5:
    marker_r,marker_c=r,c
    break
  if marker_r!=-1:break
 
 if marker_r==-1:return [[0,0,0],[0,0,0],[0,0,0]]
 
 # Find the sprite region around the marker
 # Look for a 3x3 region that contains colored pixels
 best_r,best_c=0,0
 max_count=0
 
 for r in range(max(0,marker_r-3),min(h-2,marker_r+4)):
  for c in range(max(0,marker_c-3),min(w-2,marker_c+4)):
   if r+3<=h and c+3<=w:
    count=0
    for dr in range(3):
     for dc in range(3):
      if g[r+dr][c+dc]>0 and g[r+dr][c+dc]!=5:
       count+=1
    if count>max_count:
     max_count=count
     best_r,best_c=r,c
 
 # Extract the 3x3 region
 o=[[0]*3 for _ in range(3)]
 for dr in range(3):
  for dc in range(3):
   if best_r+dr<h and best_c+dc<w:
    val=g[best_r+dr][best_c+dc]
    o[dr][dc]=val if val!=5 else 0
 
 return o