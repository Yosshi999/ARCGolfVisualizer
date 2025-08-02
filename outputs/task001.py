def p(g):
 h = [[0 for i in range(9)] for j in range(9)]
 for i in range(3):
   for j in range(3):
    for k in range(3):
     for l in range(3):
      h[i*3+k][j*3+l] = g[k][l] * (g[i][j] > 0)
 return h