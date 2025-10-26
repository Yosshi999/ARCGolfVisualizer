f=lambda g,c=0:[*zip(*[(v,(d:=1)*[-d+(d:=d+w)or(1<d<sum(v))*8for w in v])[g.count(u:=max(g))>(c:=c+(v==u))>1]for v in g])]
p=lambda g:f(f(g))