def p(g):
 h,w=len(g),len(g[0])
 o=[r[:] for r in g]
 pr1,pc1,pr2,pc2=h,w,0,0
 for r in range(h):
  for c in range(w):
   if g[r][c]==8:
    pr1,pc1=min(pr1,r),min(pc1,c)
    pr2,pc2=max(pr2,r),max(pc2,c)
 if pr1>=h:return o
 for r in range(h):
  for c in range(w):
   if g[r][c]>0 and g[r][c]!=8:
    color=g[r][c]
    nr=max(pr1,min(pr2,r))
    nc=max(pc1,min(pc2,c))
    o[nr][nc]=color
 return o