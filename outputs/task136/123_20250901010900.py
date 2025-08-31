def p(g):
 for c in[2,1]*9:
  i,j=divmod(sum(g:=[v[::-1]for v in g[::-1]],[]).index(c),10)
  if i*j:g[i-1][j-1]=c
 return g