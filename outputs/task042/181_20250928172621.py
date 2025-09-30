def p(g):
 n=sum(sum(g,[]))//24+1
 r=range(n,10-n)
 for _ in[0]*4:
  for i in r:
   for j in r:g[i-n][j+n]|=8*(g[i][j-n]==3==g[i+n][j]>g[i][j])
  g[::-1]=map(list,zip(*g))
 return g