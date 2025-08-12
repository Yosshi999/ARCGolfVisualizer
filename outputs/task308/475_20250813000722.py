e=enumerate
f=lambda g:(t:={},[[t:=t|{a:t.get(a,[])+[[y,x]]}for x,a in e(v)]for y,v in e(g)],t)[2]
def p(g):
 t = f(g)
 b = max(t,key=sum(g,[]).count)
 d = {}
 [(
  c:=t[k],
  p:=sum(sum(t[k],[])),
  q:=p-sum(map(lambda v:v[1],t[k])),
  p:=p-q,print(p,q,t[k]),
  [
   (d:=d|{(y-q//4,x-p//4):k},
    l:=max(y-q//4,x-p//4),print(y,x,q//4,p//4,l),
   )
   for y,x in t[k]
  ]
  ) for k in t if k-b]
 r = [[d.get((y,x),b) for x in range(-l,l+1)] for y in range(-l,l+1)]
 return r