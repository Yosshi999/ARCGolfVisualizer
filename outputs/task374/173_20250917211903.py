def p(g,l=9,c=1):
 for _ in'..':
  for v in g:
   for i in range(11-l):
    if{*v[i:i+l]}=={5}:v[i:i+l]=[c]*l;c=(c+3)%5
  g=[*map(list,zip(*g))]
 return l and p(g,l-1,c)or g