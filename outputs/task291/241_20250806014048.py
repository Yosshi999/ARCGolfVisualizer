def has_hole(g,x):
 l=[(i,j)for i,v in enumerate(g)for j in range(len(v))if g[i][j]==x]
 if l>[]:
  c,r=map(list,zip(*l))
  return(max(c)-min(c)+1)*(max(r)-min(r)+1)>len(c)
def p(g):
 for i in range(1,10):
  if has_hole(g,i):
   return [[i]]