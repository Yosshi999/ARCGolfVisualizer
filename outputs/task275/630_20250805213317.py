def p(g):
 h,w=len(g),len(g[0])
 if h*2==w:s=h
 elif w*2==h:s=w
 else:s=h//2
 o=[[0]*s*s for _ in range(s*s)]
 for r in range(s):
  for c in range(s):
   col=0
   if h*2==w:
    if g[r][c]!=0 and g[r][c]!=8:col=g[r][c]
    elif g[r][c+s]!=0 and g[r][c+s]!=8:col=g[r][c+s]
   elif w*2==h:
    if g[r][c]!=0 and g[r][c]!=8:col=g[r][c]
    elif g[r+s][c]!=0 and g[r+s][c]!=8:col=g[r+s][c]
   if col:
    for pr in range(s):
     for pc in range(s):
      cyan=False
      if h*2==w:
       cyan=g[pr][pc]==8 or g[pr][pc+s]==8
      elif w*2==h:
       cyan=g[pr][pc]==8 or g[pr+s][pc]==8
      if cyan:o[r*s+pr][c*s+pc]=col
 return o