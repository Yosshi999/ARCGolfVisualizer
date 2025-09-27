def p(g):
 D=lambda y,x:len(g)>y>-1<x<len(g[0])>(c:=g[y][x])>0and sum([D(y+i//3-1,x+i%3-1)for i in range(9)[g[y].__setitem__(x,-c):]],[(y,x,c)])or[];P,=[*filter(lambda l:1in[x[2]for x in l],[D(i//len(g[0]),i%len(g[0]))for i in range(len(g)*len(g[0]))])]
 for t in range(8):
  for i in range(999):
   Y=i//30-15;X=i%30-15
   if all(len(g)>y+Y>-1<x+X<len(g[0])and g[y+Y][x+X]in[0,-c][~c&1:]for y,x,c in P):
    for y,x,c in P:g[y+Y][x+X]=c
  g=t%2*g[::-1]or[*map(list,zip(*g))]
 return g