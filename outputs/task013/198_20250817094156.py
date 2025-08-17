t=lambda g:[*map(list,zip(*g))]
def p(g):
 f=g[0]==g[-1]
 if f:g=t(g)
 h=[*map(max,*g)]
 a,b=[i for i,v in enumerate(h)if v]
 g=[(h[:a]+(h[a:b+1]+h[a+1:b])*9)[:len(h)]]*len(g)
 if f:g=t(g)
 return g