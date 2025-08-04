def p(g):
 h,w=len(g),len(g[0])
 o=[[0]*5 for _ in range(5)]
 mr,mc=-1,-1
 for r in range(h):
  for c in range(w):
   if g[r][c]==3 and (mr==-1 or r<mr or (r==mr and c<mc)):
    mr,mc=r,c
 for i in range(5):
  for j in range(5):
   rr,cc=h-1-(mr+i),w-1-(mc+j)
   o[i][j]=g[rr][cc]
 return o