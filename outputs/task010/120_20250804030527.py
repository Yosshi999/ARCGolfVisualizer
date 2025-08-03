def p(g):
 a=[k:=0]*9
 for v in g:
  for i in range(9):
   if a[i]:v[i]=a[i]
   elif v[i]:
    v[i]=a[i]=k=k+1
 return g