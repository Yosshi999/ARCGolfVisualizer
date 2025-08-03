def p(g):
 g=[*map(list,zip(*g))]
 s=[(v[::-1]+[0]).index(0)for v in g]
 M,m=max(s),min([9if v<1else v for v in s])
 h=[[0]*9for _ in range(9)]
 for j in range(M):
  h[s.index(M)][j]=1
 for j in range(m):
  h[s.index(m)][j]=2
 return [*map(list,zip(*h))][::-1]