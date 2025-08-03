f=lambda x:[*map(list,zip(*x))]
def p(g):
 g=f(g)
 for i in range(15):
  c=g[i][-1]
  s=15-g[i].index(c)
  if c>0:g[i]=[0]*(15-s*2)+[c]*s+[0]*s
 return f(g)