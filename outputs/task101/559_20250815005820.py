r=range
def D(g,y,x):
 if~-(0<=y<len(g)and 0<=x<len(g[0])and(c:=g[y][x])>0):return[]
 g[y][x]-=9;return[(y,x,c)]+sum((D(g,y+a%3-1,x+a//3-1)for a in r(9)),[])
def p(g):
 g=[[0,0]+v for v in g]
 H,W=len(g),len(g[0])
 s=[D(g,y,x)for x in r(W)for y in r(H)if g[y][x]&1][0]
 s=[[(y*d+k//d,x*d+k%d,c)for y,x,c in s for k in r(d*d)]for d in[3,2,1]]
 for d in s:
  for Y in r(-H*3,H):
   for X in r(-W*3,W):
    if all(0<=y+Y<H and 0<=x+X<W and g[y+Y][x+X]==(0 if c-2 else c)for y,x,c in d):
     for y,x,c in d:g[y+Y][x+X]=c+9
 return[[a%9 for a in v[2:]]for v in g]