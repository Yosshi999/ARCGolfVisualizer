def p(g):
 for _ in'..':
  i,j=divmod(sum(g,[]).index(8),10);w=g[0]
  for v in g[:i]:w=[*map(max,w,v)];v[:]=min(g)
  g[i][j:j+2]=sorted(w,key=bool)[8:];g=g[::-1]
 return g