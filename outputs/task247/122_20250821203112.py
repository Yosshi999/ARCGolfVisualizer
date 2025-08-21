def p(g):
 f=sum(zip(*g),())
 m=max(map(f.count,{*f}-{0}))
 return[sorted([c for c in{*f}if f.count(c)==m],key=f.index)]*m