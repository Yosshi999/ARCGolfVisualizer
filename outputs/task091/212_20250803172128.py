def p(g):
 g=[*map(list,zip(*g))]
 b=-1
 for i,v in enumerate(g):
  if 5in v:
   if b<0:
    b=i;c=v.index(5);d=len(v)-v[::-1].index(5)
   else:
    h=[v[c-1:d+1]for v in g[b:i+1]]
    return [*map(list,zip(*h))]