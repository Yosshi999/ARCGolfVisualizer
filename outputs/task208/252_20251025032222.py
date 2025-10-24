r=range(21)
def p(g):
 (i,j),*_,(k,l)=[(i,j)for i in r for j in r if 0<g[i][j]not in g[0]];H=k-i-1;W=l-j-1
 for x in r[:-H]:
  for y in r[:-W]:
   if~-any(any(u[y:y+W])for u in g[x:x+H]):
    for d in r[:H+2]:g[x-1+d][y-1:y+W+1]=g[i+d][j:l+1]
 return g