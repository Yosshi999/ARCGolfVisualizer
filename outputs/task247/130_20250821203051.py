def p(g):
 f=sum(zip(*g),())
 h=[*map(f.count,{*f}-{0})]
 return[sorted([c for c in{*f}if f.count(c)==max(h)],key=f.index)]*max(h)