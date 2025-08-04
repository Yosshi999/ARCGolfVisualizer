def p(g):
 # Determine which quadrant is filled with green (3)
 quadrant=-1
 if g[0][0]==3 and g[0][1]==3 and g[1][0]==3:quadrant=0  # Top-left
 elif g[0][1]==3 and g[0][2]==3 and g[1][2]==3:quadrant=1  # Top-right  
 elif g[1][0]==3 and g[2][0]==3 and g[2][1]==3:quadrant=2  # Bottom-left
 elif g[1][2]==3 and g[2][1]==3 and g[2][2]==3:quadrant=3  # Bottom-right
 
 # Create 9x9 output
 o=[[0]*9 for _ in range(9)]
 
 # Fill first block based on quadrant
 for r in range(4):
  for c in range(4):
   rr=r if quadrant in [0,1] else r+1
   cc=c if quadrant in [0,1] else c+1
   cc=cc if quadrant in [0,3] else 9-cc-1
   o[rr][cc]=3
 
 # Fill second block
 for r in range(4):
  for c in range(4):
   rr=r+4 if quadrant in [0,1] else r+5
   cc=c+4 if quadrant in [0,1] else c+5
   cc=cc if quadrant in [0,3] else 9-cc-1
   o[rr][cc]=3
 
 return o