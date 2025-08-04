r=range(10)
def f(g):
 for i in r:
  for j in r:
   if g[i][j]==8:
    m=0
    for v in g[:i]:m=max([m]+v[:j]);v[:j]=[0]*j
    g[i][j]=m;return[*map(list,zip(*g[::-1]))]
p=lambda g:f(f(f(f(g))))