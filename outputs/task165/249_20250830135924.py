t=lambda g:[*map(list,zip(*g))]
def p(g):
 v=sum(g,[])
 C=min(c for x in range(400) if v[x:][:3]==[c:=v[x]]*3 and v.count(c)==10)
 g=t(g[::-1])
 g=[[max(w)]*b+v[b:] if C in v and any(w:=v[:(b:=v.index(C))]) else v for v in g]
 g=t(g)[::-1]
 return g