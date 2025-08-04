def p(g):
 l=len(g[0])
 for i in range(l):
  if g[-1][0]!=g[-1][i]:
   for j in range(i):g[-i-2+j][j]=g[-1][i]
   break
 return[v[:l//2]+v[:-~l//2][::-1]for v in g]