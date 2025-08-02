def p(g):
 a=[0,0,0,0]
 k=1
 for v in g:
  for i in range(4):
   if a[i]:
    v[i*2+1]=a[i]
   elif v[i*2+1]:
    v[i*2+1]=a[i]=k
    k+=1
 return g