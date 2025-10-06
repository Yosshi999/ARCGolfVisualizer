def p(g):
 for n in[len(g)]*4:
  (a,*_,c),(b,*_,d)=zip(*[(i,j)for k in range(n*n)if g[i:=k//n][j:=k%n]]);C=g[a][b];o=g[a].count(C)
  if o<g[c].count(C):
   s=b+o//2;t=d-o//2
   for v in g[:c]:v[s:t+1]=[4]*(t-s+1)
   for v in g[a+1:c]:v[b+1:d]=[4]*(d-b-1)
   for y in range(a+1):
    if s>=y:g[a-y][s-y]=4
    if t+y<n:g[a-y][t+y]=4
  g=[*map(list,zip(*g[::-1]))]
 return g