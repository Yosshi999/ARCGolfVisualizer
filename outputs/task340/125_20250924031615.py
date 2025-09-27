def p(g):
 for _ in[0]*4:g=[v[::-1]+[n+m*(m in v),m]for m,n,*v in zip(*g)]
 for v in g[2:-2]:v[2:-2]=[0]*(len(v)-4)
 return g