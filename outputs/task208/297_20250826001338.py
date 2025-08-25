r=range(21)
def p(g):
 c=min(f:=sum(g,[]),key=f.count);P=[(i,j)for i in r for j in r if g[i][j]==c];i,j=min(P);k,l=max(P);H=k-i-1;W=l-j-1
 for x in range(21-H):
  for y in range(21-W):
   if sum(sum(u[y:y+W])for u in g[x:x+H])<1:
    for d in range(H+2):g[x-1+d][y-1:y+W+1]=g[i+d][j:l+1]
 return g