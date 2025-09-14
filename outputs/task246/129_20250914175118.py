def p(g):
 for c in[3,2]:g=[[w[i]or(c in w)*any(max(g[:i+1]))*any(max(g[i:]))*8for i in range(len(g))]for w in zip(*g)]
 return g