e=enumerate
r=range
def p(g):
 L=[v[0]for v in g if len({*v})<2][0]
 n=min(v.index(L)for v in [g[0],g[-1]])+1
 g=[v[::n]+[0] for v in g[::n]]+[(len(g[0][::n])+1)*[0]]
 H,D={},{}
 for y,v in e(g[:-2]):
  for x,a in e(v[:-2]):
   if a and(b:=v[x+1]):H[a]=b;H[b]=a
   if a and(b:=g[y+1][x+1]):D[a]=b;D[b]=a
   if all([g[y][x+1],*g[y+1][x:x+3],g[y+2][x+1]]):C=g[y+1][x+1]
 s=dict(sum([[((y+q,x+p),D.get(C,0) if p*q else H[C] if p|q else C) for p in r(-1,2) for q in r(-1,2) for x,a in e(v) if a==C]for y,v in e(g)],[]))
 g=[[s[p] if (p:=(y,x))in s else a for x,a in e(v[:-1])]for y,v in e(g[:-1])]
 n=n-1
 return sum([[sum([[a]*n+[L] for a in v],[])[:-1]]*n+[[L]*(len(v)*(n+1)-1)] for v in g],[])[:-1]