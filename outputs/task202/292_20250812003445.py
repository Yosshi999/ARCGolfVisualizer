def f(g):
 if len(set(g[0])-{0})>1:
  Q=[]
  for j in range(len(g[0])):
   Q+=[g[0][j] or g[1][j]]
  for v in g:
   j=0
   while j<len(v):
    k=j
    while k<len(v)and Q[k]==Q[j]:k+=1
    if 0 in v[j:k]:
     for l in range(j,k):v[l]=0
    j=k
 return [*map(list,zip(*g))]
p=lambda g:f(f(g))