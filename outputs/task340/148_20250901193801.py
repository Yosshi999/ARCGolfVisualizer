f=lambda g:[[m:=v[0],v[1]+m*(m in v[1:])]+v[2:]for*v,in zip(*g)][::-1]
def p(g):
 g=f(f(f(f(g))))
 for v in g[2:-2]:v[2:-2]=[0]*(len(v)-4)
 return g