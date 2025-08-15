def p(g):
 for m in [2,3]:
  for s in [0,1,2]:
   t=lambda i:([0]*s*(i//m)+g[i%m])[:len(g[0])]
   for i in range(len(g)):
    if g[i]!=t(i):break
   else:return g+[t(i)for i in range(len(g),len(g[0]))]