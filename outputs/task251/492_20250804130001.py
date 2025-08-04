def p(g):
 h,w=len(g),len(g[0])
 o=[r[:] for r in g]
 for r1 in range(h):
  for c1 in range(w):
   if g[r1][c1]==2:
    for r2 in range(r1+2,h):
     for c2 in range(c1+2,w):
      if g[r2][c2]==2:
       v=1
       for c in range(c1,c2+1):
        if g[r1][c]!=2 or g[r2][c]!=2:v=0;break
       for r in range(r1,r2+1):
        if g[r][c1]!=2 or g[r][c2]!=2:v=0;break
       if v:
        for r in range(r1+1,r2):
         for c in range(c1+1,c2):
          if g[r][c]==0:o[r][c]=1
 return o