def p(g):
 h,w=len(g),len(g[0])
 o=[r[:] for r in g]
 
 # Extract the 3x3 reference pattern from top-left
 pattern=[]
 for r in range(3):
  row=[]
  for c in range(3):
   row.append(g[r][c])
  pattern.append(row)
 
 # Find blue pixels and determine where to copy pattern
 # Blue pixel at (r,c) means copy pattern to 3x3 area based on grid structure
 for r in range(h):
  for c in range(w):
   if g[r][c]==1:  # blue pixel
    # Clear the blue pixel
    o[r][c]=0
    
    # From generator: blue at [size*row+1][size*(col+1)+2]
    # This means: row*3+1 = r, (col+1)*3+2 = c
    # So: row = (r-1)//3, col+1 = (c-2)//3, col = (c-2)//3 - 1
    
    if (r-1)%3==0 and (c-2)%3==0:  # Valid blue position
     grid_row=(r-1)//3
     grid_col=(c-2)//3-1
     
     # Copy pattern to the grid cell at (grid_row, grid_col+1)
     start_r=grid_row*3
     start_c=(grid_col+1)*3+1
     
     for pr in range(3):
      for pc in range(3):
       nr,nc=start_r+pr,start_c+pc
       if 0<=nr<h and 0<=nc<w:
        o[nr][nc]=pattern[pr][pc]
 
 return o