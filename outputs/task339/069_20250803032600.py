def p(g):
 c=[v for u in g for v in u if v>0]
 return [c[0:1]*len(c)]