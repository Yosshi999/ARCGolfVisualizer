e=enumerate
r=range
R=lambda g:[*map(list,zip(*g))]
S=lambda g:sum(g,[])
M=lambda v:max(v,key=v.count)
def p(g):
 W=len(g[0]);H=len(g)//2
 if W>H*2:return R(p(R(g)))
 T=g[H:];g=g[:H];U=M(S(g));m=M(S(T))
 if len({*S(g)}-{*S(T)})>1:return p(T+g)
 def D(y,x):
  if H>y>-1<x<W>0<(c:=T[y][x])!=m:T[y][x]=m;return sum([D(y+a%3-1,x+a//3-1)for a in r(9)],[(y,x,c)])
  return[]
 s=[D(y,x)for x in r(W)for y in r(H)];B=M([a[2]for a in S(s)])
 for d in sorted(s,key=lambda d:-sum([B!=a[2]for a in d])):
  for Y in r(-H,H):
   for X in r(-W,W):
    if all([H>(q:=y+Y)>-1<(P:=x+X)<W>0<=g[q][P]==B+(c-B or U-B)for y,x,c in d]):
     for y,x,c in d:g[y+Y][x+X]=c
 return g