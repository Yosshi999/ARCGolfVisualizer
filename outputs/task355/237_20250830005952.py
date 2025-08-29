def p(g):
 s=sum(g,[]);S=sorted(s,key=s.count);T={k:sum([(k in r)+900*sum(x==k for x in r)for r in g])for k in S};del T[S[0]]
 for k in T:T[k]+=T[k]%900*(sum([k in r for r in zip(*g)])-1)
 return[[min(T,key=lambda k:T[k]//900-T[k]%900)]]