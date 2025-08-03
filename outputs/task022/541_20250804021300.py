def p(g):
 h,w=len(g),len(g[0])
 # Find gray centers
 centers=[]
 for r in range(h):
  for c in range(w):
   if g[r][c]==5:  # gray is 5
    centers.append((r,c))
 
 # Create 3x3 output with center as gray
 o=[[0 for _ in range(3)] for _ in range(3)]
 o[1][1]=5
 
 # Collect all colored pixels and their relative positions
 for cr,cc in centers:
  for dr in [-1,0,1]:
   for dc in [-1,0,1]:
    if dr==0 and dc==0:continue
    r,c=cr+dr,cc+dc
    if 0<=r<h and 0<=c<w and g[r][c]!=0 and g[r][c]!=5:
     o[dr+1][dc+1]=g[r][c]
     
 return o