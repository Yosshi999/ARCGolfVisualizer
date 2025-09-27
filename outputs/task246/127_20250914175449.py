def p(g):
 for c in 3,2:g=[[v or(c in w)*any(max(g[:i+1]))*any(max(g[i:]))*8for i,v in enumerate(w)]for w in zip(*g)]
 return g