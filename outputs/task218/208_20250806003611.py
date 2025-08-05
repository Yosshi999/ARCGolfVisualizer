def p(g):
 g=[[*filter(None,v)]for v in g if max(v)]
 g=g[:1]+[g[i+1]for i in range(len(g)-1)if g[i]!=g[i+1]]
 g=[*zip(*g)]
 g=g[:1]+[g[i+1]for i in range(len(g)-1)if g[i]!=g[i+1]]
 return[*map(list,zip(*g))]