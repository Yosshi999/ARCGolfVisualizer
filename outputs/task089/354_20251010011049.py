def p(g):
 D=lambda y,x:-1<y<13>x>=0<(c:=g[y][x])and sum([D(y+i//3-1,x+i%3-1)for i in range(9)[g[y].__setitem__(x,-c):]],[(y,x,c)])or[];r=sorted([D(i//13,i%13)for i in range(169)],key=len)
 for m in 2,3:
  if B:=[(Y,X,c)for c in r for Y,X,l in c if l==m]:
   Y,X,c=B[-1]
   for y,x,_ in B:
    for i,j,l in c:g[i-Y+y][[X-j,j-X][m>2or c==_]+x]=l
 return g