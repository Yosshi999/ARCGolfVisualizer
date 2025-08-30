t=lambda g:[*zip(*g)]
def p(g):
 v=sum(g,[])
 C=min(c for x in range(400) if v[x:][:3]==[c:=v[x]]*3 and v.count(c)==10)
 return t([v[:b]+(Q,)*(20-b) if C in v and (Q:=max(v[(b:=20-v[::-1].index(C)):])) else v for v in t(g)])