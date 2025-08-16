def f(g):
 for i in range(len(g)-2):
  for j in range(len(g[0])):
   if g[i][j]==g[i+2][j]==3and g[i+1][j]==2:
    U=V=0
    while j-U-1>=0and g[i+1][j-U-1]==3:U+=1
    while j+V+1<len(g[0])and g[i+1][j+V+1]==3:V+=1
    if U:
     for I in range(max(0,i-U+1),min(len(g),i+2+U)):
      for J in range(j,len(g[0])):g[I][J]=2if I==i+1 else 3
    if V:
     for I in range(max(0,i-V+1),min(len(g),i+2+V)):
      for J in range(j,-1,-1):g[I][J]=2if I==i+1 else 3
 return [*map(list,zip(*g))]
p=lambda g:f(f(g))