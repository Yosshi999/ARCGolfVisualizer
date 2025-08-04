def p(g):
 h,w=len(g),len(g[0])
 
 # Extract the four 2x2 regions from corners
 regions=[]
 positions=[(0,0),(0,3),(3,0),(3,3)]
 
 for r,c in positions:
  region=[]
  for dr in range(2):
   row=[]
   for dc in range(2):
    if r+dr<h and c+dc<w:
     row.append(g[r+dr][c+dc])
    else:
     row.append(0)
   region.append(row)
  regions.append(region)
 
 # Find which region is different
 # Compare each region to others to find the unique one
 for i in range(4):
  is_unique=True
  for j in range(4):
   if i!=j and regions[i]==regions[j]:
    is_unique=False
    break
  if is_unique:
   return regions[i]
 
 # If all are the same or can't determine, return first region
 return regions[0]