def p(g):
 for x in(V:=sum(g,[])):
  a,b,*_=[i for i,w in enumerate(V)if w==x]
  for i in range(a,b,9+2*(a%10<b%10)):g[i//10][i%10]=x
 return g