def p(g):
 h,w=len(g),len(g[0])
 
 # Find the yellow horizontal divider line
 divider_row=-1
 for r in range(h):
  if all(g[r][c]==4 for c in range(w)):  # yellow line
   divider_row=r
   break
 
 if divider_row==-1: return [[0]*w for _ in range(h//2)]
 
 # The output height is the height of one half
 output_h=divider_row
 o=[[0]*w for _ in range(output_h)]
 
 # XOR logic: green if exactly one half has red, black if both or neither
 for r in range(output_h):
  for c in range(w):
   top_has_red=g[r][c]==2
   bottom_r=divider_row+1+r
   bottom_has_red=False
   if bottom_r<h:
    bottom_has_red=g[bottom_r][c]==2
   
   # XOR: true if exactly one is true
   if top_has_red!=bottom_has_red:
    o[r][c]=3  # green
   else:
    o[r][c]=0  # black
 
 return o