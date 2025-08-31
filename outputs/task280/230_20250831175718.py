e=enumerate
def f(g):
 for y,v in e(g[:-1]):
  for x,_ in e(v):
   if v[x-1:x+1]==[0,2]:
    l=[*v[x:],0].index(0)
    for Y in range(y-l+1,y+l):g[Y]=[(y!=Y)+2]*x+g[Y][x:]
 return[*map(list,zip(*g))][::-1]
p=lambda g:f(f(f(f(g))))