def p(g):
 s=sum(g,[]);S=sorted(s,key=s.count);T={t:[0]*3 for t in S};del T[S[0]]
 for r in g:
  for k in T:T[k][0]+=k in r;T[k][2]+=sum(x==k for x in r)
 g=zip(*g)
 for r in g:
  for k in T:T[k][1]+=k in r
 return[[min(T,key=lambda k:T[k][2]-T[k][0]*T[k][1])]]