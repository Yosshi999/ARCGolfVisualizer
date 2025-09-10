f=lambda g,c=0:[*zip(*[[v[j]or 8*any(v[:j])*any(v[j:])for j in range(10)]if g.count(w:=max(g))>(c:=c+(v==w))>1else v for v in g])]
p=lambda g:f(f(g))