r=range
def D(g,y,x):
 try:
  if(c:=g[y][x])>0:g[y][x]-=9;return sum((D(g,y+a%3-1,x+a//3-1)for a in r(9)),[(y,x,c)])
 except:g
 return[]
def p(g):
 g=[[0,0]+v for v in g]
 H,W=len(g),len(g[0])
 s=[D(g,y,x)for x in r(W)for y in r(H)if g[y][x]&1][0]
 for d in[3,2,1]:
  for Y in r(H):
   for X in r(W):
    S=[((y*d+k//d+Y)%H,(x*d+k%d+X)%W,c)for y,x,c in s for k in r(d*d)]
    if all(g[y][x]==(0 if c-2 else c)for y,x,c in S):
     for y,x,c in S:g[y][x]=c+9
 return[[a%9 for a in v[2:]]for v in g]