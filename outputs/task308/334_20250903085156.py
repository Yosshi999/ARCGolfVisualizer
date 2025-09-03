e=enumerate
def p(g):
 G=sum(g,[]);t={}
 [[t:=t|{a:t.get(a,[])+[[y,x]]}for x,a in e(v)]for y,v in e(g)]
 d={};b=max(G,key=G.count)
 for k in t:
  if k-b:
   c=t[k];p=sum(sum(c,[]))//4;q=p-sum(map(lambda v:v[1],c))//4;p=p-q
   for y,x in c:d=d|{(y-q,x-p):k};l=max(y-q,x-p)
 r=range(-l,l+1)
 return[[d.get((y,x),b)for x in r]for y in r]