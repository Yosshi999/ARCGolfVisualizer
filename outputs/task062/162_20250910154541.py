r=range(10)
def p(g,d=4):
 for I in r:
  if({*g[I]}=={0,2})*any(g[I-1]):g=[[c or 3for c in g[min(i,I*2-i-1)]]for i in r]
 return d and p([*zip(*g)][::-1],d-1)or g