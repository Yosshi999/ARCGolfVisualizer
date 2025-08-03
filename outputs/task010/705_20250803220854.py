def p(g):
 h,w=len(g),len(g[0])
 o=[r[:]for r in g]
 
 # Find bars (columns with gray color 5)
 bars=[]
 for c in range(w):
  height=0
  for r in range(h):
   if g[r][c]==5:
    height+=1
  if height>0:
   bars.append((height,c))
 
 # Sort bars by height in descending order
 bars.sort(reverse=True)
 
 # Assign colors 1,2,3,4... based on height rank
 height_to_color={}
 for i,(height,col) in enumerate(bars):
  height_to_color[height]=i+1
 
 # Replace gray bars with ranked colors
 for c in range(w):
  bar_height=0
  for r in range(h):
   if g[r][c]==5:
    bar_height+=1
  
  if bar_height>0:
   color=height_to_color[bar_height]
   for r in range(h):
    if g[r][c]==5:
     o[r][c]=color
 
 return o