r=range
def p(g):
 g=(d:=[[5]*(W:=len(g[E:=0]))]*2)+g+d;g=[[5,5]+v+[5,5]for v in g]
 for N,L in[(3,4),(3,4),(3,3),(2,3)]:
  R=r(-L+1,L)
  for y in r(3,len(g)-3):
   for x in r(3,W):
    if(C:=(S:=[g[y+Y][x+X]+(X*Y!=0)*10 for X in R for Y in R]).count)(0)+C(12)<1<N<=C(2) and(L<4 or any(g[y+Y][x+X]&2 for Y,X in[(-3,0),(3,0),(0,-3),(0,3)])or E):
     for i in R:g[y+i][x]=11if g[y+i][x]&2else 8;g[y][x+i]=11if g[y][x+i]&2else 8;E=L>3
 return[[a%9for a in v[2:-2]]for v in g[2:-2]]