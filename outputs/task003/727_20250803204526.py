def p(g):
 h,w=len(g),len(g[0])
 o=[[0]*w for _ in range(9)]
 s=2
 for st in[2,3]:
  if h>=st*2:
   ok=1
   for off in range(st,h-st+1,st):
    for r in range(st):
     for c in range(w):
      if off+r<h:
       if g[off+r]!=g[r]and g[off+r]!=[g[r][w-1-i]for i in range(w)]:ok=0
   if ok:s=st;break
 bp=[]
 for r in range(min(s,h)):
  for c in range(w):
   if g[r][c]==1:bp.append((r,c))
 f=0
 if h>=s*2:
  fp,sp=set(),set()
  for r in range(s):
   for c in range(w):
    if r<h and g[r][c]==1:fp.add((r,c))
    if s+r<h and g[s+r][c]==1:sp.add((r,c))
  if sp=={(r,w-1-c)for r,c in fp}:f=1
 fs=0
 for off in range(0,9,s):
  for r,c in bp:
   or_,oc=off+r,c if fs==0 else w-1-c
   if or_<9:o[or_][oc]=2
  if f:fs=1-fs
 return o