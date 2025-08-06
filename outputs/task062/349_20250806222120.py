def f(g):
 g=[*map(list,zip(*g))]
 J=-1
 for i in range(len(g)):
  for j in range(len(g[0])-1):
   if 0<g[i][j]!=2 and g[i][j+1]==2 or g[i][j]==2 and 0<g[i][j+1]!=2:
    J=j+0.5
 if J>0:
  for u in g:
   for j in range(len(u)):
    if u[j]in [0,2]:
     if 0<=int(J+J-j)<10:
      u[j]=u[int(J+J-j)]or 3
     else:u[j]=3
 return g
p=lambda g:f(f(g))