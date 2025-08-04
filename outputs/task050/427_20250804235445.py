def p(g):
 h,w=len(g),len(g[0])
 o=[[g[r][c] for c in range(w)] for r in range(h)]
 d=[]
 for r in range(h):
  for c in range(w):
   if g[r][c]!=0:d.append((r,c))
 for i in range(len(d)):
  for j in range(i+1,len(d)):
   r1,c1=d[i]
   r2,c2=d[j]
   if r1==r2:
    mc,xc=min(c1,c2),max(c1,c2)
    for c in range(mc+1,xc):o[r1][c]=3
   elif c1==c2:
    mr,xr=min(r1,r2),max(r1,r2)
    for r in range(mr+1,xr):o[r][c1]=3
 return o