r=range(12)
def p(g):
 for i in r:
  for j in r:
   for d in r:
    if all(v[j:j+d+1]==[5,*[5-5*(0<y<d)]*~-d,5]for y,v in enumerate(g[i:i+d+1])):
     for v in g[i+1:i+d]:v[j+1:j+d]=[2]*~-d
 return g