def p(g):
 t=5*len(set(g[0])-{0})-1;g[0]+=[0]*(t-4)
 for i in range(t):g=[[0]+g[0][:t]]+g
 return g