def p(g):
 for r in[range(len(g))]*4:(a,b),*_,(c,d)=[(y,x)for y in r for x in r if g[y][x]];g=[[g[y][x]or((b+(y<a)<x<d-(y<a))|((y-x==a-b-2)*(x<d))|(b<x<=y+x==d+a-2))*(y<c)*(g[a].count(g[a][b])<g[c].count(g[a][b]))*4for y in r[::-1]]for x in r]
 return g