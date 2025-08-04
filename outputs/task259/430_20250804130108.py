def p(g):
 h,w=len(g),len(g[0])
 non_blue=[]
 for r in range(h):
  for c in range(w):
   if g[r][c]!=1:non_blue.append((r,c,g[r][c]))
 if not non_blue:return [[]]
 min_r=min(r for r,c,v in non_blue)
 max_r=max(r for r,c,v in non_blue)
 min_c=min(c for r,c,v in non_blue)
 max_c=max(c for r,c,v in non_blue)
 oh,ow=max_r-min_r+1,max_c-min_c+1
 o=[[0]*ow for _ in range(oh)]
 for r,c,v in non_blue:
  o[r-min_r][c-min_c]=v
 return o