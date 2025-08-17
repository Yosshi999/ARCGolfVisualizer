def p(g):
 for _ in[0]*4:
  k=sum(g,[]).index(2)
  i=k//10
  j=k%10
  g[i][j-1]=max(g[i][:j])
  g[i+1][j-1]=max(g[i+1][:j])
  g[i-1][j-1]=max(max(v[:j])for v in g[:i])
  for v in g[:i+2]:v[:j-1]=[0]*(j-1)
  g=[*map(list,zip(*g[::-1]))]
 return g