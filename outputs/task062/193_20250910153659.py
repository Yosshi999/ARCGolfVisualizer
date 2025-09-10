e=enumerate
def p(g,d=3):
 g=[*zip(*g)][::-1]
 for y,v in e(g):
  if len(set(g[y-1]))>(set(v)=={0,2})>0:g=[[c or 3 for c in(g[y*2-Y-1]if y<=Y else v)]for Y,v in e(g)]
 return d and p(g,d-1)or g