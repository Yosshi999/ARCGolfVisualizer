r=range
def p(g):
 W=len(g[0]);G=sum(g,[]);L=len(G)
 def D(z):
  if L>z>=0<(c:=G[z]):G[z]=0;return sum((D(z+a)for a in[-W,-min(1,z%W),1,W]),[z,c])
  return[]
 S=[D(z)for z in r(L)if G[z]]
 T=[v[1::2]for v in S]
 S=[v[::2]for v in S]
 for d,v in zip(S,T):
  if len(d)!=max(map(v.count,v))*2:M=(d,v)
 Q=min(v:=M[1],key=v.count)
 for d,v in zip(S,T):
  N=int((v.count(Q))**0.5)
  q=[Z for Z,C in zip(*M)if C==Q][0]
  Z=min(z for z,c in zip(d,v)if c==Q)
  s=[(j*W+k+z*N-q*N+Z,c)for z,c in zip(*M)for k in r(N)for j in r(N)]
  C=max({*v}-{Q})
  for z,c in s:G[z]=c if c==Q else C
 return[*zip(*[iter(G)]*W)]