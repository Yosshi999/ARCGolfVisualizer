def p(g):
 h,w=len(g),len(g[0])
 o=[[0 for _ in range(w)] for _ in range(h)]
 
 # Find the two colored pixels
 colors=[]
 for r in range(h):
  for c in range(w):
   if g[r][c]!=0:
    colors.append(g[r][c])
 
 if len(colors)!=2:return o
 
 c1,c2=colors[0],colors[1]
 
 # Create border patterns
 for r in range(h//2):
  # Top color borders
  o[r][0]=o[r][w-1]=c1
  o[0][r]=o[0][w-1-r]=c1
  o[2][r]=o[2][w-1-r]=c1
  # Bottom color borders
  o[h-1-r][0]=o[h-1-r][w-1]=c2
  o[h-1][r]=o[h-1][w-1-r]=c2
  o[h-3][r]=o[h-3][w-1-r]=c2
  
 return o