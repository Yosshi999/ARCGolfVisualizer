def p(g):
 h,w=len(g),len(g[0])
 o=[r[:] for r in g]
 
 # Find largest black rectangle (using original algorithm)
 best_size=-1
 best_rect=None
 
 for r2 in range(h):
  for r1 in range(r2):
   for c2 in range(w):
    for c1 in range(c2):
     # Check if rectangle is all black (sum should be 0)
     total=sum([sum(g[r][c1:c2+1]) for r in range(r1,r2+1)])
     if total: continue
     
     size=(r2-r1+1)*(c2-c1+1)
     if size>best_size:
      best_size=size
      best_rect=(r1,c1,r2,c2)
 
 # Fill the largest black rectangle with pink (6)
 if best_rect:
  r1,c1,r2,c2=best_rect
  for r in range(r1,r2+1):
   for c in range(c1,c2+1):
    o[r][c]=6
 
 return o