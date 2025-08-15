def f(g,u,v,s):
 h=[[0]*v for _ in range(u)]
 for i in range(29):
  for j in range(29):
   if (c:=h[(i+j//v*s)%u][j%v])and (d:=g[i][j]):
    if c!=d:return 0
   if g[i][j]:h[(i+j//v*s)%u][j%v]=g[i][j]
 return h
def p(g):
 P=[(6,6,0),(8,8,0),(9,18,0),(7,6,6),(4,4,0),(2,2,0),(7,7,0),(5,5,0)]
 for u,v,s in P:
  if (H:=f(g,u,v,s)):
   for i in range(len(g)):
    for j in range(len(g[0])):
     g[i][j]=H[(i+j//v*s)%u][j%v]
 return g