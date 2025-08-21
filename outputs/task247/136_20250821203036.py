def p(g):
 f=sum(zip(*g),())
 h=[*map(f.count,{*f}-{0})]
 return[sorted([c for c in range(10)if f.count(c)==max(h)],key=f.index)]*max(h)