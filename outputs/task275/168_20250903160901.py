def p(g):
 m=min(len(g),len(g[0]));a,b=[v[:m]for v in g[:m]],[v[-m:]for v in g[-m:]]
 if 8in sum(a,a):a,b=b,a
 return[[c*d/8for c in v for d in w]for v in a for w in b]