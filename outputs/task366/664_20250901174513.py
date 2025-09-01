r=range
R=lambda g:[*map(list,zip(*g))]
S=lambda g:sum(g,[])
M=lambda v:max(v,key=v.count)
def p(g):
 W=len(g[0]);H=len(g)//2
 if W>H*2:return R(p(R(g)))
 T=g[H:];g=g[:H];U=M(S(g))
 if len({*S(g)}-{*S(T)})>1:return p(T+g)
 
 H=len(T);W=len(T[0]);G=sum(T,[]);L=len(G)
 def D(z):
  if L>z>=0<(c:=G[z])!=B:G[z]=B;return sum((D(z+a)for a in[-W,-min(1,z%W),min(1,(z+1)%W),W]),[(z,c)])
  return[]
 B=M(G);s=[]
 for z in r(L):s+=D(z),
 
 G=sum(g,[])
 C=M([a[1]for a in S(s)])
 for d in sorted(s,key=lambda d:-sum([C!=a[1]for a in d])):
  for Z in r(-L,L):
   if all([L>(q:=z+Z)>=0<=G[q]==C+(c-C or U-C)for z,c in d]):
    for z,c in d:G[z+Z]=c
 return[*zip(*[iter(G)]*W)]