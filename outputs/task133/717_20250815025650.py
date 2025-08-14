r=range
def D(g,y,x):
 if~-(0<=y<len(g)and 0<=x<len(g[0])and(c:=g[y][x])>0):return[]
 g[y][x]-=99;return[(y,x,c)]+sum((D(g,y+a%3-1,x+a//3-1)for a in r(9)),[])
def p(g):
 H,W=len(g),len(g[0])
 for d in[D(g,y,x)for x in r(W)for y in r(H)]:
  if d and len(d)-max(map((v:=[0]+[q[2]for q in d]).count,v))*2:M=d
  else:
   for y,x,_ in d:g[y][x]+=99
 Q=min(v:=[q[2]for q in M],key=v.count)
 s=[[(y*d+k//d,x*d+k%d,c)for y,x,c in M for k in r(d*d)]for d in[4,3,2,1]]
 for d in s:
  for Y in r(-H*4,H):
   for X in r(-W*4,W):
    if all(0<=y+Y<H and 0<=x+X<W and g[y+Y][x+X]==Q for y,x,c in d if c==Q):
     for y,x,c in d:g[y+Y][x+X]=(max(g[y+Y][x+X]for y,x,c in d if c-Q)if c-Q else c)+99
 return[[a%99for a in v]for v in g]