r=range(99)
def p(g):
 G=sum(g,[]);D=lambda z:0<=z<100>C==G[z]and sum((D(z+a)for a in[-10,-1,1,10][:G.__setitem__(z,B)]),[z])or[];S=[];T=[];B=0
 for z in r:
  if(C:=G[z])%5:S+=D(z),;T+=C,
 B=9;C=0;U=[D(z)for z in r if G[z]<1]
 for z in sum(U,[]):G[z]=0
 for s,t in zip(S,T):
  for u in U:
   if T.count(t)<2and u==[z-s[0]+u[0]for z in s]:s=u
  for z in s:G[z]=t
 return[*zip(*[iter(G)]*10)]