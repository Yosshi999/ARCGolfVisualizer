def p(g):
 h,w=len(g),len(g[0]);R=[-1,0,1]
 for r in range(h):
  for c in range(w):
   if g[r][c]==2:
    for x in R:
     for y in R:
      I=r+x;J=c+y
      if 0<=I<h*(0<=J<w)and g[I][J]<1:g[I][J]=1
 return g