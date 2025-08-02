def p(g):
 t=sum([c!=0 for c in g[0]])
 h=[]
 for i in range(t*5):
  h+=[[0]*i+g[0][:t*5-i]+[0]*(t*5-5-i)]
 return h[::-1]