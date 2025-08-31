e=enumerate
def p(g,d=4):
 for y,v in e(g[:-1]):
  for x,_ in e(v):
   if v[x-1:x+1]==[0,2]:
    for Y in range(y-(l:=[*v[x:],0].index(0))+1,y+l):g[Y][:x]=[(y!=Y)+2]*x
 return p([*map(list,zip(*g))][::-1],d-1)if d else g