def p(g,l=9,c=0):
 for _ in'..':
  for v in g:
   for i in range(11-l):
    if{*v[i:i+l]}=={5}:v[i:i+l]=[(1,4,2)[c]]*l;c+=1
  g=[*map(list,zip(*g))]
 return l and p(g,l-1,c)or g