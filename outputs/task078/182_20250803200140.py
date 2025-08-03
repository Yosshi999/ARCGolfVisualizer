def p(g):
 g=[*map(list,zip(*g))]
 for i in range(len(g)):
  x=g[i].index(0);y=10-g[i][::-1].index(0)
  g[i]=g[i][:x]+g[i][y:]
  g[i]+=[0]*(10-len(g[i]))
 return [*map(list,zip(*g))]