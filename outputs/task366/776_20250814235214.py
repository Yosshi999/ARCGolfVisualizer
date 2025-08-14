e=enumerate
r=range
def D(g,y,x,B):
 if not(0<=y<len(g) and 0<=x<len(g[0])and(c:=g[y][x])!=B):return[]
 t=[(y,x,c)];g[y][x]=B
 for a in r(9):t+=D(g,y+a%3-1,x+a//3-1,B)
 return t

R=lambda g:[*map(list,zip(*g))]
S=lambda g:sum(g,[])
M=lambda v:max(v,key=v.count)
def p(g):
 if[v[0]for v in g if len({*v})<2]==[]:return R(p(R(g)))
 T=g[(H:=len(g)//2):]
 g=g[:H]
 if S(g).count(U:=M(S(g)))<S(T).count(V:=M(S(T))):return p((g+T)[::-1])[::-1]

 W=len(g[0])
 s=[D(T,y,x,V)for x in r(W)for y in r(H)]
 B=M([a[2]for a in sum(s,[])])
 s=sorted(s,key=lambda d:len([1for a in d if a[2]-B]))[::-1]
 for d in s:
  for Y in r(-H,H):
   for X in r(-W,W):
    if all([0<=(q:=y+Y)<H and 0<=(P:=x+X)<W and g[q][P]==(c if c-B else U)for y,x,c in d]):
     for y,x,c in d:g[y+Y][x+X]=c

 return g