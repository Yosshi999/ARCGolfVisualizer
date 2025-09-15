R=range
def p(g):
 H=len(g);W=len(g[0]);D=lambda y,x:H>y>-1<x<W>(c:=g[y][x])>0and sum([D(y+i//3-1,x+i%3-1)for i in R(9)[g[y].__setitem__(x,-c):]],[(y,x,c)])or[];P,=[*filter(lambda l:1in[x[2]for x in l],[D(i//W,i%W)for i in R(H*W)])]
 for t in R(8):
  for i in R(999):
   Y=i//30-15;X=i%30-15
   if all(H>y+Y>-1<x+X<W and g[y+Y][x+X]in[0,-c][~c&1:]for y,x,c in P):
    for y,x,c in P:g[y+Y][x+X]=c
  g,H,W=t%2*(g[::-1],H,W)or([*map(list,zip(*g))],W,H)
 return g