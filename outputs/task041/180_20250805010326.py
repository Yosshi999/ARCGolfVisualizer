r=range(10)
def f(v,x):
 if w:=[i for i in r if x==v[i]]:
  return[(v[i],x)[w[0]<=i<=w[1]]for i in r]
 return v
def p(g):
 for i in r:
  for x in r[1:]:
   g[i]=f(g[i],x)
 return g