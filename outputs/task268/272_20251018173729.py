def p(g):
 for n in[len(g)]*4:(a,b),*_,(c,d)=[(y,x)for y in range(n)for x in range(n)if g[y][x]];g=[[g[y][x]or((b+(y<a)<x<d-(y<a))|((y-x==a-b-2)*(x<d))|(b<x<=y+x==d+a-2))*(y<c)*(g[a].count(g[a][b])<g[c].count(g[a][b]))*4for y in range(n)[::-1]]for x in range(n)]
 return g