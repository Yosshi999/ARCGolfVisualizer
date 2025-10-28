e=enumerate
def p(g,d=4):
 for y,v in e(g):
  for x,_ in e(v):
   for Y in range([*v[x:],0].index(0)*([0,2]==v[x-1:x+1])):g[y+Y][:x]=g[y-Y][:x]=[(0!=Y)+2]*x
 return d and p([*map(list,zip(*g))][::-1],d-1)or g