def p(g):
 n=len(g)
 i=0
 j=0
 L=[(0,1),(1,0),(0,-1),(-1,0)]
 d=0
 for _ in[0]*n*n:
  g[i][j]=3
  x=i+L[d][0]
  y=j+L[d][1]
  X=x+L[d][0]
  Y=y+L[d][1]
  if x<0 or x>=n or y<0 or y>=n or 0<=X<n and 0<=Y<n and g[X][Y]:
   d=(d+1)%4
  else:
   i=x
   j=y
 return g