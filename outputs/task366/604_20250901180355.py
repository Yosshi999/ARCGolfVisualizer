r=range
t=lambda g:[*map(list,zip(*g))]
S=lambda g:sum(g,[])
M=lambda v:max(v,key=v.count)
def p(g):
 W=len(g[0]);H=len(g)//2
 if W>H*2:return t(p(t(g)))
 T=g[H:];g=g[:H]
 if len({*S(g)}-{*S(T)})>1:T,g=g,T
 U=M(S(g));G=S(T);L=len(G);B=M(G)
 def D(z):
  if L>z>=0<(c:=G[z])!=B:G[z]=B;return sum((D(z+a)for a in[-W,-min(1,z%W),min(1,(z+1)%W),W]),[(z,c)])
  return[]
 s=[*map(D,r(L))];G=S(g);C=M([a[1]for a in S(s)])
 for d in sorted(s,key=lambda d:-sum(C!=a[1]for a in d)):
  for Z in r(-L,L):
   if all(L>(q:=z+Z)>-1<G[q]==C+(c-C or U-C)for z,c in d):
    for z,c in d:G[z+Z]=c
 return[*zip(*[iter(G)]*W)]