def p(g):
 h,w=len(g),len(g[0])
 o=[r[:] for r in g]
 rects=[]
 for r in range(h-1):
  for c in range(w-1):
   if g[r][c]==4 and g[r][c+1]==4 and g[r+1][c]==4:
    min_r,max_r,min_c,max_c=r,r+1,c,c+1
    while max_r+1<h and all(g[max_r+1][cc]==4 for cc in range(min_c,max_c+1)):
     max_r+=1
    while max_c+1<w and all(g[rr][max_c+1]==4 for rr in range(min_r,max_r+1)):
     max_c+=1
    while min_r-1>=0 and all(g[min_r-1][cc]==4 for cc in range(min_c,max_c+1)):
     min_r-=1
    while min_c-1>=0 and all(g[rr][min_c-1]==4 for rr in range(min_r,max_r+1)):
     min_c-=1
    area=(max_r-min_r+1)*(max_c-min_c+1)
    rect=(area,min_r,max_r,min_c,max_c)
    if rect not in rects:
     rects.append(rect)
 rects.sort()
 for i,(area,min_r,max_r,min_c,max_c) in enumerate(rects):
  fill_val=1 if i==0 else 2
  for r in range(min_r+1,max_r):
   for c in range(min_c+1,max_c):
    o[r][c]=fill_val
 return o