r=range(21)
def p(g):
 c=sum({*sum(g,[])}-{*g[0]});(i,j),*_,(k,l)=[(i,j)for i in r for j in r if g[i][j]==c];H=k-i-1;W=l-j-1
 for x in r[:-H]:
  for y in r[:-W]:
   if sum(sum(u[y:y+W])for u in g[x:x+H])<1:
    for d in r[:H+2]:g[x-1+d][y-1:y+W+1]=g[i+d][j:l+1]
 return g