def p(g):
 for c in[1,2]*9:
  i,j=divmod(sum(g,[]).index(c),10)
  if i*j:g[i-1][j-1]=c
  g=[v[::-1]for v in g][::-1]
 return g