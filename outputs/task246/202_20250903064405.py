e=enumerate
def p(g):
 F=lambda c:min(v.index(c)for v in g if c in v);a,b=sorted([F(2),p:=F(3)]);s=0
 for y,v in e(g):
  Q=sum(v);s^=Q>0
  if Q==2:v[a+1:b]=[8]*(b-a-1)
  if(s|Q)&3&(Q-3):v[p]=8
 return g