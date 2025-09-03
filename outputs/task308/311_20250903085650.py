e=enumerate
def p(g):
 G=sum(g,[]);
 d={};b=max(G,key=G.count)
 for k in G:
  if k!=b:
   c=[[y,x]for y,v in e(g)for x,a in e(v) if a==k]
   p=sum(sum(c,[]))//4;q=p-sum(map(lambda v:v[1],c))//4;p=p-q
   for y,x in c:d=d|{(y-q,x-p):k};l=max(y-q,x-p)
 r=range(-l,l+1)
 return[[d.get((y,x),b)for x in r]for y in r]