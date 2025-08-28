def p(g):
 l=len(g)//2
 for i in range(l+1):
  if g[-2][i]:
   for j in range(i):g[-i-2+j][j]=g[-1][i]
   return[v[:l]+v[l::-1]for v in g]