e=enumerate
def p(g):
 G=sum(g,[]);W=len(g[0]);b=max(G,key=G.count);d={};l=0
 for k in{*G}-{b}:
  c=[z for z,a in e(G)if a==k];q=sum(c)//4
  for z in c:l=max(l,(q-z)//W);d|={z-q:k}
 r=range(-l,l+1)
 return[[d.get(y*W+x,b)for x in r]for y in r]