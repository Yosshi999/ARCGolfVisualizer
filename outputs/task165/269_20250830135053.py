t=lambda g:[*map(list,zip(*g))]
def p(g):
 v=sum(g,[])
 C=min(c for x,c in enumerate(v) if v[x:][:3]==[c]*3 and v.count(c)==10)
 Q=max({*v}-{C})
 g=t(g[::-1])
 g=[[Q]*b+v[b:] if C in v and Q in v and v.index(Q)<(b:=v.index(C)) else v for v in g]
 g=t(g)[::-1]
 return g