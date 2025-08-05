r=range(11)
def p(g):
 for v in g:
  for i in r:
   for j in r:
    if min(v[i:j]+[c:=max(g[0][i:j]+[0])]):v[i:j]=[c]*(j-i)
 return g