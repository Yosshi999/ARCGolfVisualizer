e=enumerate
def p(g):
 g=[*zip(*g)];f=lambda c:min(v.index(c)for v in g if c in v);g=[(v,(v*3)[f(m:=max(v))-f(1)+len(v):][:len(v)])[m>0]for v in g]
 return[*zip(*g)]