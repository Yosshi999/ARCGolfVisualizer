def f(g):
 return[*map(list,zip(*[[(3,x)[v.count(0)+v.count(3)<len(v)-2or x>0]for x in v]for v in g]))]
p=lambda g:f(f(g))