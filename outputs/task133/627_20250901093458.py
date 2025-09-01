r=range
def D(g,y,x,W):
 if len(g)>y>-1<x<W>0<(c:=g[y][x]):g[y][x]=0;return sum((D(g,y+a%3-1,x+a//3-1,W)for a in r(9)),[(y,x,c)])
 return[]
def p(g):
 H,W=len(g),len(g[0])
 S=[D(g,y,x,W)for x in r(W)for y in r(H) if g[y][x]>0]
 for d in S:
  if len(d)!=max(map((v:=[q[2]for q in d]).count,v))*2:M=d
 Q=min(v:=[q[2]for q in M],key=v.count)
 for d in S:
  N=int(([c for _,_,c in d].count(Q))**0.5)
  q,p=[(Y,X)for Y,X,C in M if C==Q][0]
  Y,X=min((y,x) for y,x,c in d if c==Q)
  s=[(y*N+k//N-q*N+Y,x*N+k%N-p*N+X,c)for y,x,c in M for k in r(N*N)]
  C=max({c for _,_,c in d}-{Q})
  for y,x,c in s:g[y][x]=c if c==Q else C
 return g