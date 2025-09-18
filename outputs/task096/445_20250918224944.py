e=enumerate
def p(g):
 f=sum(g,[])
 C=max(f,key=f.count)
 P={}
 for d in range(6):
  for c in {*f}:
   for x in range(20):
    for y in range(-1,19):
     S={(abs(i-x),abs(j-y)):c for i,v in e(g)for j,w in e(v)if w==c}
     if c not in P.values() and {*map(max,S)}=={d} and all((abs(i-x),abs(j-y)) not in S for i,v in e(g)for j,w in e(v)if w!=c):
      P|=S
 l=max(max(P))
 r=range(-l,l+1)
 return[[P.get((abs(i),abs(j)),C)for j in r]for i in r]