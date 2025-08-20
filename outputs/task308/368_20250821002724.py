e=enumerate
f=lambda g:(t:={},[[t:=t|{a:t.get(a,[])+[[y,x]]}for x,a in e(v)]for y,v in e(g)],t)[2]
p=lambda g:(t:=f(g),d:={},[(c:=t[k],p:=sum(sum(t[k],[]))//4,q:=p-sum(map(lambda v:v[1],t[k]))//4,p:=p-q,[(d:=d|{(y-q,x-p):k},l:=max(y-q,x-p))for y,x in t[k]]) for k in t if k-(b:=max(t,key=sum(g,[]).count))],r:=range(-l,l+1),[[d.get((y,x),b) for x in r]for y in r])[-1]