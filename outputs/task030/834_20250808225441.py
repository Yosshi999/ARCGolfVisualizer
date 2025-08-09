def p(g):
 h,w=len(g),len(g[0])
 o=[[0 for _ in range(w)] for _ in range(h)]
 
 # Find colored clusters
 clusters={}
 for r in range(h):
  for c in range(w):
   if g[r][c]!=0:
    color=g[r][c]
    if color not in clusters:
     clusters[color]=[]
    clusters[color].append((r,c))
 
 if not clusters:return o
 
 # Find the topmost cluster position
 min_r=min(min(r for r,c in coords) for coords in clusters.values())
 
 # Move all clusters to the same vertical position as the topmost one
 blue_min_r=min(r for r,c in clusters[1])
 for color,coords in clusters.items():
  # Find cluster's bounding box
  cluster_min_r=min(r for r,c in coords)
  offset=blue_min_r-cluster_min_r
  print(color,offset)
  
  # Place cluster at aligned position
  for r,c in coords:
   new_r=r+offset
   if 0<=new_r<h:
    o[new_r][c]=color
    
 return o