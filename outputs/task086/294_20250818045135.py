r=range
def p(g):
 for y in r(len(g)):
  for x in r(len(g[0])):
   if(A:=g[y][x])>0:
    d=g[y][x+3]>0;B=g[y+1][x+1]
    for Y in r(-d-1,4+d*2):
     for X in r(-d-1,4+d*2):g[Y+y][X+x]=-A if 0<X<d+2>Y>0else-B if 0<=X<d+3>Y>=0else-A if 0<=Y&X<d+3else g[Y+y][X+x]
 return[[*map(abs,v)]for v in g]