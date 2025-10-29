def p(g):
 m=len(g[0]);b=g[m:]
 if 8in max(a:=g[:m]):a,b=b,a
 return[[c*d/8for c in v for d in w]for v in a for w in b]or[*zip(*p([*zip(*g)]))]