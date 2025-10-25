def D(g,y,x,c):
 if-1<x<len(g)>y>=0<c==g[y][x]:g[y][x]=0;return sum((D(g,y+a%3-1,x+a//3-1,c)for a in range(9)),[(y,x)])
 return[]
def p(g,n=16):
 l=len(g)-1
 for k in range(l*l):
  if(c:=g[i:=k//l][j:=k%l])>0<3<len({*g[i][j:j+2]+g[i+1][j:j+2]}):
   for u,v in D(eval(str(g)),i,j,c):g[2*i+1-u][v]|=g[i+1][j]
 return n and p([*map(list,zip(*g[::2*(n%8<1)-1]))],n-1)or g