e=enumerate
def p(g):
 F=lambda c:min(v.index(c)for v in g if c in v);a,b=sorted([F(2),p:=F(3)]);s=0
 for y,v in e(g):
  s^=sum(v)>0
  if 2 in v:v[a+1:b]=[8]*(b-a-1)
  if(s|(2 in v))*~-(3 in v):v[p]=8
 return g