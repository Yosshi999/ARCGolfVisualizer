def p(g):
 G=[*map(list,zip(*g))]
 v=[-1,*(i for i,v in enumerate(G)if~-any(v)),len(g[0])]
 H=[G[l+1:r]for l,r in zip(v,v[1:])if l+1<r]
 Y=[]
 to=None
 for a in H:
  color,*_={*sum(a,[])}-{0,5}
  if to is not None:
   a[0][fr:=a[0].index(5)]=color
   a=[v[fr-to:]+v[:fr-to]for v in a]
  if 5 in a[-1]:
   a[-1][to:=a[-1].index(5)]=color
  Y.extend(a)
 return[*map(list,zip(*Y))]