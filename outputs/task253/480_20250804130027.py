def p(g):
 h,w=len(g),len(g[0])
 o=[[0]*4 for _ in range(4)]
 for r in range(h-1):
  for c in range(w-1):
   v1,v2,v3,v4=g[r][c],g[r][c+1],g[r+1][c],g[r+1][c+1]
   if v1!=0 and v1==v2 and v1==v3 and v4==0:
    o[0][0]=o[0][1]=o[1][0]=v1
   elif v1!=0 and v1==v2 and v3==0 and v1==v4:
    o[0][2]=o[0][3]=o[1][3]=v1
   elif v1!=0 and v2==0 and v1==v3 and v1==v4:
    o[2][0]=o[3][0]=o[3][1]=v1
   elif v1==0 and v2!=0 and v2==v3 and v2==v4:
    o[2][3]=o[3][2]=o[3][3]=v2
 return o