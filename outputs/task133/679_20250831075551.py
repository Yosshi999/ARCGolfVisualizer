r=range
def D(g,y,x,W):
 if len(g)>y>-1<x<W>0<(c:=g[y][x]):g[y][x]-=99;return sum((D(g,y+a%3-1,x+a//3-1,W)for a in r(9)),[(y,x,c)])
 return[]
def p(g):
 H,W=len(g),len(g[0])
 for d in[D(g,y,x,W)for x in r(W)for y in r(H)]:
  if d and len(d)-max(map((v:=[0]+[q[2]for q in d]).count,v))*2:M=d
  for y,x,_ in d:g[y][x]+=99
 Q=min(v:=[q[2]for q in M],key=v.count);s=[[(y*d+k//d,x*d+k%d,c)for y,x,c in M for k in r(d*d)]for d in[4,3,2,1]]
 for d in s:
  for Y in r(-H*4,H):
   for X in r(-W*4,W):
    if all(c-Q or H>y+Y>-1<x+X<W>Q==g[y+Y][x+X]for y,x,c in d):
     for y,x,c in d:g[y+Y][x+X]=(max(g[y+Y][x+X]for y,x,c in d if c-Q)if c-Q else c)+99
 return[[a%99for a in v]for v in g]