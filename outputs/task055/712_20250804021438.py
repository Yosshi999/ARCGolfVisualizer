def p(g):
 h,w=len(g),len(g[0])
 o=[r[:] for r in g]
 hr=[r for r in range(h) if all(g[r][c]==8 for c in range(w))]
 vc=[c for c in range(w) if all(g[r][c]==8 for r in range(h))]
 if len(hr)<2 or len(vc)<2:return o
 hr.sort()
 vc.sort()
 r0,r1=hr[0],hr[1]
 c0,c1=vc[0],vc[1]
 cm=[1,2,3,4,6]
 for r in range(0,r0):
  for c in range(c0+1,c1):
   if g[r][c]!=8:o[r][c]=cm[1]
 for r in range(r0+1,r1):
  for c in range(0,c0):
   if g[r][c]!=8:o[r][c]=cm[3]
 for r in range(r0+1,r1):
  for c in range(c0+1,c1):
   if g[r][c]!=8:o[r][c]=cm[4]
 for r in range(r0+1,r1):
  for c in range(c1+1,w):
   if g[r][c]!=8:o[r][c]=cm[2]
 for r in range(r1+1,h):
  for c in range(c0+1,c1):
   if g[r][c]!=8:o[r][c]=cm[0]
 return o