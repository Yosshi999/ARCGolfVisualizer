def p(g):
 for d in range(1,10):
  if all(len({*sum([v[k::d]for v in g[k::d]],[])}-{0})==1for k in range(d)):
   return[[max(sum([v[j%d::d]for v in g[i%d::d]],[]))for j in range(21)]for i in range(21)]