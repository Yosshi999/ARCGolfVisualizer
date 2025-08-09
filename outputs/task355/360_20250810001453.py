def p(g):
 S=[i/10for i in range(10)]
 for v in g:
  for u in v:S[u]+=1
 Z=sum(v>=1for v in S)
 T={S.index(c):[0]*3 for c in sorted(S)[-Z+1:]}
 for r in g:
  for k,v in T.items():
   v[0]+=k in r
   v[2]+=sum(x==k for x in r)
 g=[*map(list,zip(*g))]
 for r in g:
  for k,v in T.items():v[1]+=k in r
 return [[sorted(T,key=lambda k:T[k][2]-T[k][0]*T[k][1])[0]]]