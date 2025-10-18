def p(g):
 for n in[len(g)]*4:
  (a,b),*_,(c,d)=[(k//n,k%n)for k in range(n*n)if g[k//n][k%n]]
  if g[a].count(g[a][b])<g[c].count(g[a][b]):g=[[g[y][x]or((b+(y<a)<x<d-(y<a))|((y-x==a-b-2)*(x<d))|(b<x<=y+x==d+a-2))*(y<c)*4for x in range(n)]for y in range(n)]
  g=[*map(list,zip(*g[::-1]))]
 return g