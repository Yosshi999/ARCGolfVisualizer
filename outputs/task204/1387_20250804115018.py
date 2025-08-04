def p(g):
 h,w=len(g),len(g[0])
 o=[r[:] for r in g]
 
 # Find rectangular outlines and fill them
 visited=[[False]*w for _ in range(h)]
 
 for r in range(h):
  for c in range(w):
   if g[r][c]==1 and not visited[r][c]:
    # Try to identify a rectangle starting from this corner
    if (r+1<h and g[r+1][c]==1 and 
        c+1<w and g[r][c+1]==1):
     # Find rectangle dimensions
     length=1
     while c+length<w and g[r][c+length]==1:
      length+=1
     height=1
     while r+height<h and g[r+height][c]==1:
      height+=1
     
     # Check if this forms a valid rectangle outline
     valid=True
     if height==length:  # Square
      # Check top and bottom edges
      for cc in range(c,c+length):
       if cc<w and (g[r][cc]!=1 or g[r+height-1][cc]!=1):
        valid=False
        break
      # Check left and right edges
      if valid:
       for rr in range(r,r+height):
        if rr<h and (g[rr][c]!=1 or g[rr][c+length-1]!=1):
         valid=False
         break
      
      if valid:
       # Fill interior
       fill_color=7 if length%2==1 else 2
       for rr in range(r+1,r+height-1):
        for cc in range(c+1,c+length-1):
         if rr<h and cc<w:
          o[rr][cc]=fill_color
       
       # Mark as visited
       for rr in range(r,r+height):
        for cc in range(c,c+length):
         if rr<h and cc<w:
          visited[rr][cc]=True
 
 return o