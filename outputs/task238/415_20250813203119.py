e=enumerate
r=range
f=lambda g:min([y for y,v in e(g)if len(set(v)-{0,8})])
p=lambda g:(
 n:=max(s:=[y for y,v in e(g)if 8 in v])-(t:=min(s))+1,
 l:=min([v.index(8) for v in g if 8 in v]),
 q:=f(g),
 p:=f([*zip(*g)]),
 [[ (0 if g[t+y-1][l+x-1]-8 else g[q+[1,n+1,0,1][k:=(i>0)*2+(j>0)]][p+[0,1,1,n+1][k]] if (i:=x-y)*(j:=x+y-n-1) else 8) if 0<x<n+1 and 0<y<n+1 else g[q+y][p+x] for x in r(n+2)]for y in r(n+2)]
)[-1]