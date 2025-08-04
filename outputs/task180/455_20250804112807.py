def p(g):
 h,w=len(g),len(g[0])
 s=h//2
 o=[[0 for c in range(s)] for r in range(s)]
 
 # Extract quadrants - colors 4,5,6,9 from positions (0,0),(0,1),(1,0),(1,1)
 # Order of overlay: 0,3,2,1 which is colors 4,9,6,5
 colors=[4,5,6,9]
 offsets=[(0,0),(0,1),(1,0),(1,1)]
 order=[0,3,2,1]
 
 for idx in order:
  color=colors[idx]
  ro,co=offsets[idx]
  for r in range(s):
   for c in range(s):
    if g[ro*s+r][co*s+c]==color:
     o[r][c]=color
 
 return o