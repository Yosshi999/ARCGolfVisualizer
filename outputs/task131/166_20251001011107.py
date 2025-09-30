def p(g):
 for _ in[0]*4:
  *g,=zip(*g[::-1]);i,*_,j,k=[i for i,v in enumerate(g)if max(v)]
  if{*g[k]}=={2}:g[:k]=g[-1:]*(k-j+i-2)+[[8]*len(g[0])]+g[i:j+1]
 return g