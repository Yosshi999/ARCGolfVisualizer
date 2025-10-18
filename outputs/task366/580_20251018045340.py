r=range
t=lambda g:[*map(list,zip(*g))]
S=lambda g:sum(g,[])
M=lambda v:max(v,key=v.count)
def p(g):
 W=len(g[0]);H=len(g)//2
 if W>H*2:return t(p(t(g)))
 T=g[H:];g=g[:H]
 if len({*S(g)}-{*S(T)})>1:T,g=g,T
 U=M(S(g));G=S(T);L=len(G);B=M(G);D=lambda z:L>z>=0<(c:=G[z])!=B and sum((D(z+a)for a in[-~z%W>0,W][:G.__setitem__(z,B)]),[(z,c)])or[];s=[*map(D,r(L))];G=S(g);C=M([a[1]for a in S(s)])
 for d in sorted(s,key=lambda d:-sum(C!=a[1]for a in d)):
  for Z in r(-L,L):
   if all(L>(q:=z+Z)>-1<G[q]==C+(c-C or U-C)for z,c in d):
    for z,c in d:G[z+Z]=c
 return[*zip(*[iter(G)]*W)]