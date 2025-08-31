e=enumerate
r=range
def D(g,y,x,B,w):
 if~-(len(g)>y>-1<x<w>0<(c:=g[y][x])!=B):return[]
 g[y][x]=B;return sum([D(g,y+a%3-1,x+a//3-1,B,w)for a in r(9)],[(y,x,c)])
R=lambda g:[*map(list,zip(*g))]
S=lambda g:sum(g,[])
M=lambda v:max(v,key=v.count)
def p(g):
 W=len(g[0]);H=len(g)//2
 if W>H*2:return R(p(R(g)))
 T=g[H:];g=g[:H];U=M(S(g))
 if len({*S(g)}-{*S(T)})>1:return p(T+g)
 s=[D(T,y,x,M(S(T)),W)for x in r(W)for y in r(H)];B=M([a[2]for a in S(s)])
 for d in sorted(s,key=lambda d:-sum([B!=a[2]for a in d])):
  for Y in r(-H,H):
   for X in r(-W,W):
    if all([H>(q:=y+Y)>-1<(P:=x+X)<W>0<=g[q][P]==B+(c-B or U-B)for y,x,c in d]):
     for y,x,c in d:g[y+Y][x+X]=c
 return g