def p(g):
 f=sum(g,[])
 h=[*map(f.count,{*f}-{0})]
 return[sorted([c for c in range(10)if f.count(c)==max(h)],key=lambda x:f.index(x)%10)]*max(h)