def p(g):
 t,*h=len(set(g[0])-{0}),
 for i in range(t*5):h=[[0]*i+g[0][:t*5-i]+[0]*(t*5-5-i)]+h
 return h