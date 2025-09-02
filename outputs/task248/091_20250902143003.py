def p(g):
 i=0;x=-1
 for v in g[::-1]:
  v[i]=1
  if i in[0,len(v)-1]:x=-x
  i+=x
 return g