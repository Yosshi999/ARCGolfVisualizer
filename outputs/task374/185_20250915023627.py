def p(g):
 c=0
 for l in range(9,0,-1):
  for _ in'..':
   for v in g:
    for i in range(11-l):
     if{*v[i:i+l]}=={5}:v[i:i+l]=[(1,4,2)[c]]*l;c+=1
   g=[*map(list,zip(*g))]
 return g