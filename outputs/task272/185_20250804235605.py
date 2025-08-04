def p(g):
 h=len(g);w=len(g[0])
 for i in range(h):
  for j in range(w):
   if g[i][j]:g[i][j]-=(i and g[i-1][j])|(j and g[i][j-1])|(i<h-1and g[i+1][j])|(j<w-1and g[i][j+1])<1
 return g