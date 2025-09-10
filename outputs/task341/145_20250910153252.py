f=lambda g,c=0:[*zip(*[(v,[v[j]or 8*any(v[:j])*any(v[j:])for j in range(10)])[g.count(w:=max(g))>(c:=c+(v==w))>1]for v in g])]
p=lambda g:f(f(g))