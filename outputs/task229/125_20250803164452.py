def p(g):
 a = [0]*10
 for u in g:
  for v in u:a[v]+=1
 c = a.index(max(a))
 return [[5if v!=c else c for v in u]for u in g]