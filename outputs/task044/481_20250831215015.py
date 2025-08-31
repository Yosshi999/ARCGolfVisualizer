r=range
def p(g):
 G=sum(g,[])
 def D(z):
  if 0<=z<100 and (c:=G[z])==C:G[z]=B;return sum((D(z+a)for a in[-10,-1,1,10]),[z])
  return[]
 S=[];T=[];B=0
 for z in r(100):
  if~-((C:=G[z])in[0,5]):S+=D(z),;T+=C,
 U=[];B=-1;C=0
 for z in r(100):
  if G[z]==0:U+=D(z),
 A=[]
 for u in U:
  c=0
  for s,t in zip(S,T):
   if T.count(t)==1 and u==[z-s[0]+u[0]for z in s]:c=t;A+=t,
  for z in u:G[z]=c
 for s,t in zip(S,T):
  if~-(t in A):
   for z in s:G[z]=t
 return[*zip(*[iter(G)]*10)]