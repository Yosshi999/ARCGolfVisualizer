def p(g):
 h,w=len(g),len(g[0])
 o=[r[:] for r in g]
 gr,gc,yr,yc=-1,-1,-1,-1
 for r in range(h):
  for c in range(w):
   if g[r][c]==3:
    gr,gc=r,c
   elif g[r][c]==4:
    yr,yc=r,c
 nr,nc=gr,gc
 if gr<yr:nr+=1
 elif gr>yr:nr-=1
 if gc<yc:nc+=1
 elif gc>yc:nc-=1
 o[gr][gc]=0
 o[nr][nc]=3
 return o