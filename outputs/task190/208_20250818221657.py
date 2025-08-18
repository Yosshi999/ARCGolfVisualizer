r=range(8)
def p(g):
 for _ in[0]*4:
  for i in r:
   for j in r:
    if g[i][j]*g[i+1][j+1]*g[i+1][j+2]:
     x=i;y=j
     while min(x,y)>=0:g[x][y]=g[i][j];x-=1;y-=1
  g=[*map(list,zip(*g[::-1]))]
 return g