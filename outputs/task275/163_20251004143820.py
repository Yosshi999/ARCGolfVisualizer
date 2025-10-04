def p(g):
 m=len(g[0])
 if len(g)<m:return[*zip(*p([*zip(*g)]))]
 a=g[:m];b=g[m:]
 if 8in max(a):a,b=b,a
 return[[c*d/8for c in v for d in w]for v in a for w in b]