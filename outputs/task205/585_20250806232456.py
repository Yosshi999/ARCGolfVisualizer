def p(g):
 Hs=[]
 for i in range(len(g)):
  for j in range(len(g[0])):
   for k in range(i+2,len(g)):
    for l in range(j+2,len(g[0])):
     C=set(v for u in g[i:k+1] for v in u[j:l+1])
     if len(C)==2:
      Hs.append([u[j:l+1] for u in g[i:k+1]])
     elif len(C)>2:
      break
 h=max(Hs,key=lambda h:len(h)*len(h[0]))
 C=set(v for u in h for v in u)
 c=list(C-{h[0][0]})[0]
 H=[[*v]for v in h]
 for i,v in enumerate(h):
  if c in v:H[i]=[c]*len(v)
 h=[*map(list,zip(*h))]
 H=[*map(list,zip(*H))]
 for i,v in enumerate(h):
  if c in v:H[i]=[c]*len(v)
 return [*map(list,zip(*H))]