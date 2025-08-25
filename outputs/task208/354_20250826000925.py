def p(g):
 f=sum(g,[])
 c=min(f,key=f.count)
 P=[(i,j)for i in range(21)for j in range(21)if g[i][j]==c]
 i,j=min(P)
 k,l=max(P)
 H=k-i-1
 W=l-j-1
 for x in range(1,21-H):
  for y in range(1,21-W):
   if sum(sum(u[y:y+W])for u in g[x:x+H])<1:
    g[x-1][y-1:y+W+1]=g[x+H][y-1:y+W+1]=[c]*(W+2)
    for I in range(x-1,x+H+1):g[I][y-1]=g[I][y+W]=c
 return g