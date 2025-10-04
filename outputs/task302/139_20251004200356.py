e=enumerate
def p(g,b=0):
 for y,v in e(g):
  for x,c in e(v):
   if c:
    if all(g[y-1][b+1:x]):l=x+~b;v[b+1:x]=[5+l]*l
    b=x
 return g