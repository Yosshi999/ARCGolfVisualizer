f=lambda g:g[:1]+[g[i+1]for i in range(len(g)-1)if g[i]!=g[i+1]]
def p(g):
 g=[[*filter(None,v)]for v in g if max(v)]
 g=f(g)
 g=[*zip(*g)]
 g=f(g)
 return[*map(list,zip(*g))]