r=range
def p(g):
 W=len(g[0]);G=sum(g,[]);L=len(G)
 def D(z):
  if L>z>=0<(c:=G[z]):G[z]=0;return sum((D(z+a)for a in[-W,-min(1,z%W),1,W]),[(z,c)])
  return[]
 S=[D(z)for z in r(L)if G[z]]
 for d in S:
  if len(d)!=max(map((v:=[q[1]for q in d]).count,v))*2:M=d
 Q=min(v:=[q[1]for q in M],key=v.count)
 for d in S:
  N=int(([c for _,c in d].count(Q))**0.5)
  q=[Z for Z,C in M if C==Q][0]
  Z=min(z for z,c in d if c==Q)
  s=[(j*W+k+z*N-q*N+Z,c)for z,c in M for k in r(N)for j in r(N)]
  C=max({c for _,c in d}-{Q})
  for z,c in s:G[z]=c if c==Q else C
 return[*zip(*[iter(G)]*W)]