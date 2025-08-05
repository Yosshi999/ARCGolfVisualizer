def p(g):
 l=len(g[0])
 for i in range(l):
  if(c:=g[-1][i])!=g[-1][0]:
   for j in range(i):g[-i-2+j][j]=c
   return[v[:l//2]+v[l//2::-1]for v in g]