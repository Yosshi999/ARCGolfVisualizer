def p(g):
 h,w=len(g),len(g[0])
 o=[r[:] for r in g]
 cr,cc,bc=0,0,0
 for r in range(h):
  for c in range(w):
   if g[r][c]>0:
    cnt=sum(1 for rr in range(h) for cc2 in range(w) if g[rr][cc2]==g[r][c])
    if cnt==1: cr,cc,bc=r,c,g[r][c]
 if not bc: return o
 lr=sum(1 for r in range(h) if g[r][cc]>0 and r<cr)
 rr=sum(1 for r in range(h) if g[r][cc]>0 and r>cr)
 uc=sum(1 for c in range(w) if g[cr][c]>0 and c<cc)
 dc=sum(1 for c in range(w) if g[cr][c]>0 and c>cc)
 if rr>lr:
  for r in range(cr+1,h):
   if o[r][cc]==0: o[r][cc]=bc
 elif lr>rr:
  for r in range(cr):
   if o[r][cc]==0: o[r][cc]=bc
 elif dc>uc:
  for c in range(cc+1,w):
   if o[cr][c]==0: o[cr][c]=bc
 elif uc>dc:
  for c in range(cc):
   if o[cr][c]==0: o[cr][c]=bc
 return o