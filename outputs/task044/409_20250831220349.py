r=range
def p(g):
 G=sum(g,[])
 def D(z):
  if 0<=z<100>G[z]==C:G[z]=B;return sum((D(z+a)for a in[-10,-1,1,10]),[z])
  return[]
 S=[];T=[];B=0
 for z in r(100):
  if(C:=G[z])%5:S+=D(z),;T+=C,
 U=[];B=9;C=0
 for z in r(100):
  if G[z]<1:U+=D(z),
 for z in sum(U,[]):G[z]=0
 for s,t in zip(S,T):
  for u in U:
   if T.count(t)<2and u==[z-s[0]+u[0]for z in s]:s=u
  for z in s:G[z]=t
 return[*zip(*[iter(G)]*10)]