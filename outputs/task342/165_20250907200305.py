def p(g):
 for _ in'..':
  i,j=divmod(sum(g,[]).index(8),10);w=g[0]
  for v in g[:i]:w=[*map(max,w,v)];v[:]=min(g)
  g[i][j:j+2]=[*filter(int,w)];g=g[::-1]
 return g