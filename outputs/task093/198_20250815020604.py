def f(v):
 if len({*v})<3:return[*v]
 l=min(i for i,x in enumerate(v)if x==5)
 a=v[:l].count(0)
 b=v[l:].count(0)
 return[0]*a+[5]*(14-a-b)+[0]*b
q=lambda g:[f(v)for v in zip(*g)]
p=lambda g:q(q(g))