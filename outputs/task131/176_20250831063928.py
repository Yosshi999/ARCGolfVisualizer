def p(g):
 for _ in[0]*4:
  g=[*zip(*g)][::-1];m=[]
  for v in g:
   if 2 in v:g=(m+[*filter(any,g)]+[[8 for _ in v]]+[g[0]]*99)[:len(g)]
   if any(v):break
   m+=[v]
 return g