e=enumerate
f=lambda g:[*map(list,zip(*(t:=sum([
  (d:=sum([w[x::2][:2]for w in g[y::2][:2]],[]),
   [(y+k+3,x+k+3) for k in range(9)] if not 0 in d and len(d)>3 and d.count(b:=d[0])==1 else [])[1]
for x,a in e(g[0])for y,v in e(g)],[]),[[b if(y,x)in t else a for x,a in e(v)]for y,v in e(g)])[1]))][::-1]
p=lambda g:f(f(f(f(g))))