def p(g):
 for v in g:
  for i in range(len(v)//2):
   v[i]=v[-i-1]=0
 return g