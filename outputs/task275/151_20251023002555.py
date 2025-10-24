def p(g):
 m=len(g[0]);a=g[:m];b=g[m:]
 if 8in max(a):a,b=b,a
 return m<5and[[c*d/8for c in v for d in w]for v in a for w in b]or[*zip(*p([*zip(*g)]))]