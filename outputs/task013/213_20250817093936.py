e=enumerate
t=lambda g:[*map(list,zip(*g))]
def p(g):
 f=max(g[0]+g[-1])<1
 if f:g=t(g)
 h=[*map(max,*g)]
 a,b=[i for i,v in e(h)if v]
 h=(h[:a]+(h[a:b+1]+h[a+1:b])*9)[:len(h)]
 g=[h]*len(g)
 if f:g=t(g)
 return g