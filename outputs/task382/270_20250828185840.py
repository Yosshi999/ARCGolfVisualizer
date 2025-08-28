def p(g):
 c=0
 for _ in'..':
  for _ in'.'*4:
   c+=1
   if 8in g[0] and 8 not in g[1] and 2in [*zip(*g)][0]:
    print(c,g)
    for v,w in zip(g[1:],g):
     if 2in v:
      v[:]=[2]+w[:-1]
     else:v[:]=[0]+w[1:]
   g=[*map(list,zip(*g[::-1]))]
  g=g[::-1]
 return g