R=[-1,1]
def p(g):
 r=range(n:=len(g))
 for i in r:
  for j in r:
   if(c:=g[i][j]):
    for x in R:
     for y in R:
      I=i;J=j
      while 0<=I<n*(0<=J<n):g[I][J]=c;I+=x;J+=y
    return g