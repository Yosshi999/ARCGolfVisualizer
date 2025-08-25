def p(g):
 if g[0]==g[-1]:return[*zip(*p([*zip(*g)]))]
 h=[*map(max,*g)];a,b=[i for i,v in enumerate(h)if v];return[(h[:a]+(h[a:b+1]+h[a+1:b])*9)[:len(h)]]*len(g)