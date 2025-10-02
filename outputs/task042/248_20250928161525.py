def p(g):
 n=sum(sum(g,[]))//24+1
 for _ in'..':
  for t in range(162*n*n):
   if g[y:=t%9][x:=t//9%9]==3==g[y+1][x+1]>g[y][x+1]>=0<=(q:=y-(Y:=t//81%n+n)+(Z:=Y+t//81//n%n+n+1)*(F:=t//81//n//n))<10>(p:=x-Y+Z*(1-F))>=0:g[q][p]=8
  g=g[::-1]
 return g