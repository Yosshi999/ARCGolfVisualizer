def p(g):
 c=set([v for u in g for v in u])-{5}
 c=list(c)[0]
 return [[0if v!=5else c for v in u]for u in g]