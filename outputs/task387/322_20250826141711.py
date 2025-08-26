r=range
f=lambda g:[y for y,v in enumerate(g)if any(v)]
def p(g):
 h,w=f(g),f(zip(*g))
 for t in r(36):
  for k in r((h[1]-h[0])//2)[1::2]:g[h[a:=t//2%2]+(k+1)*(1-2*a)][w[b:=t%2]]=5
  for k in r((w[1]-w[0])//2)[1::2]:g[h[b]][w[a]+(k+1)*(1-2*a)]=5
  if(Y:=t//4%3-1)|(X:=t//12%3-1):g[h[b]+Y][w[a]+X]=g[h[~b]][w[a]]
 return g