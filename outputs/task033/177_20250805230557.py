def p(g):
 for i in range(3):
  for j in range(3):
   for y in range(5):
    for x in range(5):
     g[i*6+y][j*6+x]=(g[i*6+y][j*6+x],g[5][0])[g[i*6+y][j*6+x]<g[y][x]]
 return g