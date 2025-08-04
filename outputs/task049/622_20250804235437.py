def p(g):
 h,w=len(g),len(g[0])
 v=[[False]*w for _ in range(h)]
 r=[]
 for row in range(h):
  for col in range(w):
   if g[row][col]!=0 and not v[row][col]:
    c=g[row][col]
    mr,xr,mc,xc=row,row,col,col
    for rr in range(h):
     for cc in range(w):
      if g[rr][cc]==c:
       mr,xr=min(mr,rr),max(xr,rr)
       mc,xc=min(mc,cc),max(xc,cc)
       v[rr][cc]=True
    ww,hh=xc-mc+1,xr-mr+1
    r.append((c,mr,mc,xr,xc,ww*hh))
 if not r:return [[]]
 r.sort(key=lambda x:x[5])
 c,mr,mc,xr,xc,a=r[0]
 o=[]
 for rr in range(mr,xr+1):
  ro=[]
  for cc in range(mc,xc+1):
   ro.append(g[rr][cc])
  o.append(ro)
 return o