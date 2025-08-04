def p(g):
 h,w=len(g),len(g[0])
 colors=[]
 for r in range(h):
  for c in range(w):
   colors.append(g[r][c])
 mode=max(set(colors),key=colors.count)
 o=[[0]*w*h for _ in range(h*w)]
 for r in range(h):
  for c in range(w):
   if g[r][c]==mode:
    for dr in range(h):
     for dc in range(w):
      o[r*h+dr][c*w+dc]=g[dr][dc]
 return o