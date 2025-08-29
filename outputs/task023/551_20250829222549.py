def q(g,u,G):
 I=lambda i,j:len(g)>i>-1<j<len(g[0]);D=lambda u:(u//len(g[0]),u%len(g[0]));h=[*map(list,g)];i,j=D(u);B=lambda i,j,Y,X:all(I(i+y,j+x)and h[i+y][j+x]==5for y,x in zip(Y,X))
 for s in range(len(G)):
  for t in range(len(G[0])):h[i+s][j+t]=G[s][t]
 while u<len(g)*len(g[0]):
  i,j=D(u)
  if B(i,j,[0,0,1,1],[0,1]*2)and(h:=q(h,u,[[8,8],[8,8]]))[i][j]!=5or B(i,j,[0]*3,[0,1,2])and(h:=q(h,u,[[2,2,2]]))[i][j]!=5or B(i,j,[0,1,2],[0]*3)and(h:=q(h,u,[[2],[2],[2]]))[i][j]!=5:return h
  if h[i][j]==5:return g
  u+=1
 return h
p=lambda g:q(g,0,[])