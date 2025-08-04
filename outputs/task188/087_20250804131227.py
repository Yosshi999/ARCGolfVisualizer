def p(g):
 v=[l[:len(g[0])//2]for l in g]
 return[g[:len(g)//2],v][[l*2 for l in v]==g]