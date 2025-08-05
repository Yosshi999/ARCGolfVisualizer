def p(g):
 l=len(g[0])//2
 for i in range(l+1):
  if(c:=g[-1][i])!=g[-1][0]:
   for j in range(i):g[-i-2+j][j]=c
   return[v[:l]+v[l::-1]for v in g]