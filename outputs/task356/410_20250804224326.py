def p(g):
 h,w=len(g),len(g[0])
 o=[r[:] for r in g]
 points=[]
 for r in range(h):
  for c in range(w):
   if g[r][c]==8:
    points.append((r,c))
 for i in range(len(points)):
  for j in range(i+1,len(points)):
   r1,c1=points[i]
   r2,c2=points[j]
   if r1==r2:
    for c in range(min(c1,c2),max(c1,c2)+1):
     o[r1][c]=8
   if c1==c2:
    for r in range(min(r1,r2),max(r1,r2)+1):
     o[r][c1]=8
 return o