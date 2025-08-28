def p(g):
 for _ in'..':
  for _ in'.'*4:
   if 8in g[0]and sum(g[1])<1and max(g)[0]==2:
    for v,w in zip(g[1:],g):v[:]=([0]+w[1:],[2]+w[:-1])[2in v]
   g=[*map(list,zip(*g[::-1]))]
  g=g[::-1]
 return g