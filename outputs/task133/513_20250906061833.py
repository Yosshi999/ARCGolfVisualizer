r=range
def p(g):
 W=len(g[0]);G=sum(g,[]);L=len(G);D=lambda z:L>z>=0<(c:=G[z])and sum((D(z+a)for a in[-1,-W,1,W][z%W<1:G.__setitem__(z,0)]),[(z,c)])or[];S=[(v:=D(z),[a[1]for a in v])for z in r(L)if G[z]]
 for M,P in S:
  if len(P)-max(map(f:=P.count,P))*2:break
 Q=min(P,key=f);F=lambda v:min(z for z,c in v if c==Q)
 for d,X in S:
  N=int(X.count(Q)**0.5);C=max({*X}-{Q});q=F(M);Z=F(d);s=[(j*W+k+z*N-q*N+Z,c)for z,c in M for k in r(N)for j in r(N)]
  for z,c in s:G[z]=C+(c==Q)*(c-C)
 return[*zip(*[iter(G)]*W)]