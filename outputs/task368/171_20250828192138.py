def p(g):
 h=[[w for w in v if w%5]for v in g if{*v}-{0,5}]
 for k in range(99):
  if g[i:=k//10][j:=k%10]==5:
   for v,w in zip(g[i:i+len(h)],h):v[j:j+len(w)]=w
 return g