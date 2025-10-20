r=range
f=lambda g:[*map(g.index,filter(any,g))]
def p(g):
 h=f(g);w=f([*zip(*g)])
 for t in r(36):
  for k in r(1,(h[1]-h[0])//2,2):g[h[a:=t//2%2]-~k*(1-2*a)][w[b:=t%2]]=5
  for k in r(1,(w[1]-w[0])//2,2):g[h[b]][w[a]-~k*(1-2*a)]=5
  if(Y:=t//4%3-1)|(X:=t//12%3-1):g[h[b]+Y][w[a]+X]=g[h[~b]][w[a]]
 return g