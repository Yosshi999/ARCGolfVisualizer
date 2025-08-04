def p(g):
 h,w=len(g),len(g[0])
 colors=set()
 for r in range(h):
  for c in range(w):
   if g[r][c]!=0:colors.add(g[r][c])
 colors=len(colors)
 o=[[0]*w for _ in range(h)]
 for r in range(h):
  for c in range(w):
   o[r][c]=(r+c)%colors+1
 return o