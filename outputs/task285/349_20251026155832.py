def p(g,n=16):
 l=len(g)-1
 for k in range(l*l):
  if 3<len({*g[i:=k//l][(j:=k%l):j+2]+g[i+1][j:j+2]}):
   for u,v in(D:=lambda h,y,x:-1<x<l>y>=0<g[i][j]==h[y][x]and(exec('h[y][x]=0')or sum((D(h,y+a%3-1,x+a//3-1)for a in range(9)),[(y,x)]))or[])(eval(str(g)),i,j):g[2*i+1-u][v]|=g[i+1][j]
 return n and p([*map(list,zip(*g[::2*(n%8<1)-1]))],n-1)or g