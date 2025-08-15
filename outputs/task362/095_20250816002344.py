def p(g):
 o=sum(v==5for v in sum(g,[]))
 return [v[o:-1]+v[:1]+v[:o]for v in g[-o:]*2+g[o:-o]]