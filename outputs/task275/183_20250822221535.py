def p(g):
 m=min(len(g),len(g[0]));a,b=[v[:m]for v in g[:m]],[v[-m:]for v in g[-m:]]
 if any(max(v)==8for v in a):a,b=b,a
 return[[c*(d==8)for c in v for d in w]for v in a for w in b]