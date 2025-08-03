def p(g):
 h,w=len(g),len(g[0])
 # Count non-zero colors
 from collections import Counter
 flat=[g[r][c] for r in range(h) for c in range(w) if g[r][c]>0]
 if not flat:return g
 counter=Counter(flat)
 rarest=min(counter,key=counter.get)
 # Find bounding box of rarest color
 min_r,min_c,max_r,max_c=h,w,-1,-1
 for r in range(h):
  for c in range(w):
   if g[r][c]==rarest:
    min_r,min_c=min(min_r,r),min(min_c,c)
    max_r,max_c=max(max_r,r),max(max_c,c)
 # Crop to bounding box
 if max_r==-1:return g
 o=[]
 for r in range(min_r,max_r+1):
  row=[]
  for c in range(min_c,max_c+1):
   row.append(g[r][c])
  o.append(row)
 return o