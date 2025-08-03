def p(g):
 h,w=len(g),len(g[0])
 ms=3
 o=[[0 if g[r][c]!=5 else 5 for c in range(w)] for r in range(h)]
 color=0
 for r in range(h):
  for c in range(w):
   if g[r][c]>0 and g[r][c]!=5:
    color=g[r][c]
    break
  if color:break
 if not color:return o
 m={}
 for r in range(h):
  for c in range(w):
   if g[r][c]==color:
    mr,mc=r//(ms+1),c//(ms+1)
    m[(mr,mc)]=m.get((mr,mc),0)+1
 if not m:return o
 max_cnt=max(m.values())
 for (mr,mc),cnt in m.items():
  if cnt==max_cnt:
   sr,sc=mr*(ms+1),mc*(ms+1)
   for dr in range(ms):
    for dc in range(ms):
     if o[sr+dr][sc+dc]!=5:
      o[sr+dr][sc+dc]=color
 return o