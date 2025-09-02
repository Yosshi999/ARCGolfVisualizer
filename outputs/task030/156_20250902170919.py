e=enumerate
def p(g):
 l=len(g);g=[*zip(*g)];f=lambda c:min(v.index(c)for v in g if c in v);g=[(v*3)[f(max(v)or 1)-f(1)+l:][:l]for v in g]
 return[*zip(*g)]