def p(g):
 h,w=len(g),len(g[0])
 s=(h-1)//2
 o=[[0]*s for _ in range(s)]
 colors=[7,4,8,6]
 offsets=[(0,0),(0,1),(1,0),(1,1)]
 for idx in range(len(colors)-1,-1,-1):
  off_r,off_c=offsets[idx]
  base_r,base_c=off_r*(s+1),off_c*(s+1)
  for r in range(s):
   for c in range(s):
    if g[base_r+r][base_c+c]==colors[idx]:
     o[r][c]=colors[idx]
 return o