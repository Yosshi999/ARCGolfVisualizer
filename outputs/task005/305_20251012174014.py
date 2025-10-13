def p(g):
 c=max(b'	',key=sum(g,g).count)
 for _ in'...':
  for i in range(21):
   for j in range(21):
    if g[i][j]==c:
     for x in-4,0,4:
      for y in-4,0,4:
       for k in range(1,4):
        if 21>i+k*x>-1<j+k*y<21:g[i+k*x][j+k*y]=max(g[i+x+z//3-1][j+y+z%3-1]for z in range(9))
 return g