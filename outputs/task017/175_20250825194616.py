r=range(21)
def p(g):
 for d in range(5,10):
  if len({*sum([v[1::d]for v in g[2::d]],[])}-{0})==1:
   return[[max(sum([v[j%d::d]for v in g[i%d::d]],[]))for j in r]for i in r]