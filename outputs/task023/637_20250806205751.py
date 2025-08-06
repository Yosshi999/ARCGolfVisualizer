def q(g,u,G):
 I=lambda i:0<=i<len(g)
 J=lambda j:0<=j<len(g[0])
 D=lambda u:(u//len(g[0]),u%len(g[0]))
 h=[[*v]for v in g]
 i,j=D(u)
 for s in range(len(G)):
  for t in range(len(G[0])):
   h[i+s][j+t]=G[s][t]
 while u<len(g)*len(g[0]):
  i,j=D(u)
  if h[i][j]==5:
   if I(i+1)and J(j+1)and h[i][j+1]==h[i+1][j]==h[i+1][j+1]==5:
    if (h:=q(h,u,[[8,8],[8,8]]))[i][j]!=5:return h
   if J(j+1)and J(j+2)and h[i][j+1]==h[i][j+2]==5:
    if (h:=q(h,u,[[2,2,2]]))[i][j]!=5:return h
   if I(i+1)and I(i+2)and h[i+1][j]==h[i+2][j]==5:
    if (h:=q(h,u,[[2],[2],[2]]))[i][j]!=5:return h
   return g
  u+=1
 return h
def p(g):
 return q(g,0,[])