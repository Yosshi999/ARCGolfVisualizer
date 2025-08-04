def p(g):
 h,w=len(g),len(g[0])
 o=[r[:] for r in g]
 v=[[0]*w for _ in range(h)]
 for r in range(h):
  for c in range(w):
   if g[r][c]==5 and not v[r][c]:
    for s in range(3,min(h-r,w-c)+1):
     if r+s-1<h and c+s-1<w:
      valid=True
      for i in range(s):
       if g[r][c+i]!=5 or g[r+s-1][c+i]!=5 or g[r+i][c]!=5 or g[r+i][c+s-1]!=5:
        valid=False
        break
      if valid:
       for i in range(1,s-1):
        for j in range(1,s-1):
         if g[r+i][c+j]!=0:
          valid=False
          break
        if not valid:break
      if valid:
       for i in range(1,s-1):
        for j in range(1,s-1):
         o[r+i][c+j]=5+s-2
       for i in range(s):
        for j in range(s):
         v[r+i][c+j]=1
       break
 return o