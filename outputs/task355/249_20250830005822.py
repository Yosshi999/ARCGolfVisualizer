def p(g):
 s=sum(g,[]);S=sorted(s,key=s.count);T={k:sum([30*(k in r)+900*sum(x==k for x in r)for r in g])for k in S};del T[S[0]];g=[*zip(*g)]
 for k in T:T[k]+=sum([k in r for r in g])
 return[[min(T,key=lambda k:T[k]//900-(T[k]%30)*(T[k]//30%30))]]