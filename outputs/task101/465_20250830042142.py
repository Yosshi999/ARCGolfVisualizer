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
  for Z in r(H*W):
   b=1;S=[(q,p,c)for y,x,c in s for k in r(d*d)if(b:=b&(g[q:=(y*d+k//d+Z//W)%H][p:=(x*d+k%d+Z)%W]==c&2))]
   for y,x,c in S:g[y][x]|=b*(c+9)
 return[[a%9 for a in v[2:]]for v in g]