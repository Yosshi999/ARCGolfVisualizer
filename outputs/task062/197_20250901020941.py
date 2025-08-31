e=enumerate
def f(g):
 g=[*zip(*g)][::-1]
 for y,v in e(g):
  if len(set(g[y-1]))>(set(v)=={0,2})>0:g=[[c or 3 for c in(g[y*2-Y-1]if y<=Y else v)]for Y,v in e(g)]
 return g
p=lambda g:f(f(f(f(g))))