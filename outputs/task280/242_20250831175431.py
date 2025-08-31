e=enumerate
def f(g):
 G=[*map(list,zip(*g))]
 for y,v in e(g[:-1]):
  for x,_ in e(v):
   if G[x][y-1:y+1]==[0,2]:
    l=[*G[x][y:],0].index(0)
    for X in range(x-l+1,x+l):G[X]=[(x!=X)+2]*y+G[X][y:]
 return G[::-1]
p=lambda g:f(f(f(f(g))))