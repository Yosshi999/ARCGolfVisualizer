def p(g):
 m=len(g[0]);a=g[:m];b=g[m:]
 if 4<m:return[*zip(*p([*zip(*g)]))]
 if 8in max(a):a,b=b,a
 return[[c*d/8for c in v for d in w]for v in a for w in b]