def p(g):
 g=[*map(list,zip(*g))]
 v=[i for i,v in enumerate(g)if~-any(v)]+[len(g)]
 Y=[]
 l=-1
 for r in v:
  if l+1<r:
   a=g[l+1:r]
   c=sum({*sum(a,[])})-5
   if 5 in a[0]:a[0][f:=a[0].index(5)]=c;a=[v[f-t:]+v[:f-t]for v in a]
   if 5 in a[-1]:a[-1][t:=a[-1].index(5)]=c
   Y+=a
  l=r
 return[*zip(*Y)]