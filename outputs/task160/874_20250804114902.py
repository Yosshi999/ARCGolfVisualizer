def p(g):
 h,w=len(g),len(g[0])
 o=[r[:] for r in g]
 sprites=[]
 for r in range(h-2):
  for c in range(w-2):
   if g[r][c]==1:
    pattern=[]
    for dr in range(3):
     for dc in range(3):
      if r+dr<h and c+dc<w:
       pattern.append(g[r+dr][c+dc])
      else:
       pattern.append(0)
    if pattern==[1,1,1,1,0,1,1,1,1]:
     sprites.append((r,c,0))
     for dr in range(3):
      for dc in range(3):
       o[r+dr][c+dc]=0
     o[r][c+1]=2
     o[r+1][c]=2
     o[r+1][c+1]=2
     o[r+1][c+2]=2
     o[r+2][c+1]=2
    elif pattern==[0,1,0,1,1,1,0,1,0]:
     sprites.append((r,c,1))
    elif pattern==[0,0,0,0,0,0,0,1,1]:
     sprites.append((r,c,2))
    elif pattern==[1,1,0,1,1,0,0,0,0]:
     sprites.append((r,c,3))
    elif pattern==[1,0,0,1,0,0,1,1,1]:
     sprites.append((r,c,4))
    elif pattern==[0,0,0,0,1,1,0,1,1]:
     sprites.append((r,c,5))
 return o