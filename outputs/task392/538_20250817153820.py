def f(g,m,u,v):
 c,=[*set(sum(g,[]))-{0}]
 h=[[*r]for r in g]
 for i in range(10):
  for j in range(10):
   b=int(max(abs(i-u),abs(j-v)))%m==1
   if b<1and g[i][j]:return 0
   h[i][j]=c if b else 5
 return h
def p(g):
 for i in range(10):
  if (G:=f(g,2,i,0)):return G
  if (G:=f(g,2,i,9)):return G
  if (G:=f(g,2,0,i)):return G
  if (G:=f(g,2,9,i)):return G
 for j in [-0.5,0.5]:
  for i in range(10):
   if (G:=f(g,3,i+j,j)):return G
   if (G:=f(g,3,i+j,9+j)):return G
   if (G:=f(g,3,j,i+j)):return G
   if (G:=f(g,3,9+j,i+j)):return G