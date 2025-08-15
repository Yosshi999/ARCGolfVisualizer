T=lambda g:[*map(list,zip(*g))]
def p(g):
 v=[-1,*(i for i,v in enumerate(T(g))if~-any(v)),len(g[0])]
 Y=t=[]
 for a in[T(g)[l+1:r]for l,r in zip(v,v[1:])if l+1<r]:
  c,*_={*sum(a,[])}-{0,5}
  if 5 in a[0]:a[0][f:=a[0].index(5)]=c;a=[v[f-t:]+v[:f-t]for v in a]
  if 5 in a[-1]:a[-1][t:=a[-1].index(5)]=c
  Y+=a
 return T(Y)